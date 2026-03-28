import os
import re
import unicodedata
from TTS.api import TTS
from pydub import AudioSegment, silence

# --------------------------------------------------
# DEVICE SELECTION
# --------------------------------------------------

def get_tts_device():
    forced = os.getenv("FORCE_TTS_DEVICE")
    if forced:
        return forced
    return "cpu"


TTS_DEVICE = get_tts_device()

# Enable fallback (safe on Mac)
os.environ["PYTORCH_ENABLE_MPS_FALLBACK"] = "1"

tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2").to(TTS_DEVICE)

# --------------------------------------------------
# Supported XTTS Languages
# --------------------------------------------------

SUPPORTED_XTTS_LANGS = [
    "en", "es", "fr", "de", "it", "pt",
    "pl", "tr", "ru", "nl",
    "cs", "ar", "zh", "ja", "ko", "hi"
]

# -----------------------
# Text Cleaning
# -----------------------

def clean_text(text: str):
    text = unicodedata.normalize("NFKC", text)
    text = text.replace("\n", " ").strip()
    text = re.sub(r'[\u200B-\u200D\uFEFF]', '', text)
    return text


# -----------------------
# Sentence Splitting
# -----------------------

def split_sentences(text: str):
    pattern = r'(?<=[.!?।。！？؟…])\s*'
    sentences = re.split(pattern, text)
    return [s.strip() for s in sentences if s.strip()]


# -----------------------
# Smart Chunking (balanced)
# -----------------------

def enforce_chunk_limit(sentences, max_len=80):
    chunks = []

    for s in sentences:
        if len(s) <= max_len:
            chunks.append(s)
        else:
            words = s.split()
            temp = ""

            for w in words:
                if len((temp + " " + w).strip()) < max_len:
                    temp += " " + w
                else:
                    chunks.append(temp.strip())
                    temp = w

            if temp:
                chunks.append(temp.strip())

    return chunks


# -----------------------
# Silence Trimming (SAFE)
# -----------------------

def trim_silence(audio: AudioSegment):
    chunks = silence.split_on_silence(
        audio,
        min_silence_len=120,                # slightly higher → safer
        silence_thresh=audio.dBFS - 35,     # less aggressive
        keep_silence=50                     # keep natural transitions
    )

    if not chunks:
        return audio

    combined = chunks[0]
    for c in chunks[1:]:
        combined += c

    return combined


# -----------------------
# Main TTS Function
# -----------------------

def synthesize_voice(text: str, language: str, speaker_wav: str):

    if language not in SUPPORTED_XTTS_LANGS:
        raise ValueError(f"Language '{language}' not supported by XTTS")

    if not os.path.exists(speaker_wav):
        raise FileNotFoundError(f"Speaker file not found: {speaker_wav}")

    text = clean_text(text)

    # Language-specific fixes
    if language == "ja":
        text = text.replace("。", "。 ")
    if language == "hi":
        text = text.replace("।", ". ")

    sentences = split_sentences(text)
    sentences = enforce_chunk_limit(sentences)

    combined_audio = AudioSegment.empty()

    for i, sentence in enumerate(sentences):

        if not sentence.strip():
            continue

        temp_output = f"temp_sentence_{i}.wav"

        # 🔥 KEEP STABLE — no aggressive tuning
        tts.tts_to_file(
            text=sentence,
            speaker_wav=speaker_wav,
            language=language,
            file_path=temp_output,
            temperature=0.6,
            repetition_penalty=1.5,
            length_penalty=1.0,
            speed=0.95
        )

        segment_audio = AudioSegment.from_wav(temp_output)

        # 🔥 Trim only excess silence (not speech)
        segment_audio = trim_silence(segment_audio)

        print(f"[TTS] Sentence {i} | chars={len(sentence)} | duration={len(segment_audio)} ms")

        combined_audio += segment_audio

        os.remove(temp_output)

    # -----------------------
    # Duration Alignment
    # -----------------------

    original_audio = AudioSegment.from_wav(speaker_wav)

    if len(combined_audio) > len(original_audio):
        combined_audio = combined_audio[:len(original_audio)]
    else:
        combined_audio += AudioSegment.silent(
            duration=(len(original_audio) - len(combined_audio))
        )

    # -----------------------
    # Export final audio
    # -----------------------

    final_output = "final_tts_output.wav"
    combined_audio.export(final_output, format="wav")

    return final_output