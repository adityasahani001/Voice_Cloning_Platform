from supabase import create_client

SUPABASE_URL = "YOUR_SUPABASE_URL"
SUPABASE_KEY = "YOUR_SUPABASE_KEY"

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)


# ------------------ VIDEO ------------------

def insert_video(data):
    return supabase.table("videos").insert(data).execute()


# ------------------ JOB ------------------

def create_job(data):
    return supabase.table("jobs").insert(data).execute()


def update_job(job_id, data):
    return supabase.table("jobs").update(data).eq("id", job_id).execute()