# 🎬 Multiva AI — Cross-Lingual Auto Dubbing Platform

## 🚀 Overview

Multiva AI is an AI-powered auto dubbing platform designed to translate and dub videos into multiple languages while preserving the speaker's voice, tone, and lip synchronization. The system leverages modern speech recognition, machine translation, voice cloning, and lip-sync technologies to deliver high-quality multilingual video outputs efficiently.

---

## ❗ Problem Statement

### 1. Language Barrier in Content Consumption

A massive portion of global video content is locked behind language barriers, limiting accessibility and reach.

### 2. Expensive & Time-Consuming Dubbing

Traditional dubbing involves:

* Hiring voice actors
* Recording studios
* Manual synchronization
* Post-production editing

This process is:

* Costly 💰
* Slow ⏳
* Not scalable 📉

### 3. Lack of Voice Consistency

Most existing AI dubbing tools fail to:

* Preserve original speaker identity
* Maintain emotional tone
* Deliver natural voice output

### 4. Poor Lip Synchronization

Mismatch between audio and lip movement reduces viewer immersion.

---

## 💡 Solution

Multiva AI solves these problems using an end-to-end AI pipeline that:

* 🎙 Converts speech to text using ASR
* 🌍 Translates text into target languages
* 🧠 Clones speaker voice using neural TTS
* 🎥 Synchronizes lips with generated speech

### Key Highlights

* ⚡ Fast processing (~2 minutes per video)
* 🌐 Multi-language support
* 🎭 Voice cloning with speaker preservation
* 🎬 Automated lip-sync
* 💸 Cost-efficient vs traditional dubbing

---

## 🧠 System Architecture

```
Input Video
   ↓
Audio Extraction
   ↓
Speech-to-Text (ASR)
   ↓
Machine Translation
   ↓
Text-to-Speech (Voice Cloning)
   ↓
Lip Sync (Wav2Lip)
   ↓
Final Dubbed Video Output
```

---

## ⚙️ Tech Stack

### 🔊 Speech Recognition

* Whisper (medium)

### 🌐 Translation

* Facebook NLLB (fb-nllb-v2-600M)

### 🗣 Text-to-Speech (Voice Cloning)

* YourTTS
* VALL-E X (experimental)

### 🎥 Lip Sync

* Wav2Lip

### 🗄 Backend & Database

* Supabase (PostgreSQL)

### ☁️ Storage

* Cloudflare R2 (for video storage)

### 🖥 Frontend

* HTML, CSS, JavaScript

---

## 🔄 Pipeline Breakdown

### 1. Audio Extraction

* Extract audio from input video using FFmpeg

### 2. Speech Recognition (ASR)

* Convert speech into text
* Model: Whisper Medium

### 3. Translation

* Translate extracted text into target language
* Model: NLLB-600M

### 4. Voice Cloning (TTS)

* Generate speech in target language
* Preserve speaker identity

### 5. Lip Synchronization

* Sync generated speech with original video
* Model: Wav2Lip

### 6. Video Reconstruction

* Merge synced video with generated audio

---

## 📊 Performance

| Feature             | Result     |
| ------------------- | ---------- |
| Avg Processing Time | ~2 minutes |
| Voice Similarity    | ~85%       |
| Lip Sync Accuracy   | High       |
| Cost Efficiency     | Very High  |

---

## 🧪 Challenges & Innovations

### Challenges

* Maintaining voice identity across languages
* Aligning translated speech timing
* Lip sync accuracy for different phonemes

### Innovations

* Medium-model optimization for faster inference
* Balanced trade-off between speed and quality
* Modular pipeline for scalability

---

## 🔐 Why Multiva AI?

| Feature     | Multiva AI | Traditional Dubbing |
| ----------- | ---------- | ------------------- |
| Cost        | Low        | High                |
| Speed       | Fast       | Slow                |
| Scalability | High       | Limited             |
| Automation  | Full       | Manual              |

---

## 🛠 Setup & Installation

```bash
# Clone the repository
git clone https://github.com/your-username/multiva-ai.git
cd multiva-ai

# Install dependencies
pip install -r requirements.txt

# Run the backend
python app.py
```

---

## 📦 API Workflow (Example)

```json
POST /upload
{
  "video": "file"
}

POST /process
{
  "language": "hi"
}

GET /output
```

---

## 🌍 Use Cases

* 🎓 Educational content localization
* 🎥 YouTube creators expanding globally
* 📢 Marketing & advertisements
* 🏢 Enterprises & training videos

---

## 🚧 Future Scope

* Real-time dubbing
* Emotion-aware voice cloning
* More language support
* Web3 integration for creator monetization

---

## 👥 Team

* Aditya
* Nikhil
* Mudit 


---

## 📜 License

MIT License

---

## ⭐ Contribute

Pull requests are welcome. For major changes, please open an issue first.

---

## 💬 Contact

For queries or collaborations:

* Email: [your-email@example.com](mailto:your-email@example.com)
* GitHub Issues

---

> Built with ❤️ using AI to break language barriers
