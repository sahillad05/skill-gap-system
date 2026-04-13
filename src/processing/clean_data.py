import json
import re

# -------- TEXT CLEANING FUNCTION --------
def clean_text(text):
    if not text:
        return ""
    
    text = text.lower()  # lowercase
    text = re.sub(r"http\S+", "", text)  # remove links
    text = re.sub(r"[^a-zA-Z\s]", "", text)  # remove special chars
    text = re.sub(r"\s+", " ", text).strip()  # remove extra spaces
    
    return text


# -------- CLEAN JOB DATA --------
def clean_jobs():
    with open("data/jobs_raw.json", "r") as f:
        data = json.load(f)

    cleaned_jobs = []

    for job in data.get("results", []):
        cleaned_job = {
            "title": clean_text(job.get("title")),
            "description": clean_text(job.get("description")),
            "location": job.get("location", {}).get("display_name", ""),
            "salary": job.get("salary_min")
        }
        cleaned_jobs.append(cleaned_job)

    with open("data/jobs_cleaned.json", "w") as f:
        json.dump(cleaned_jobs, f, indent=4)

    print("✅ Jobs cleaned!")


# -------- CLEAN YOUTUBE DATA --------
def clean_youtube():
    with open("data/youtube_raw.json", "r") as f:
        data = json.load(f)

    cleaned_videos = []

    for vid in data:
        cleaned_video = {
            "skill": vid.get("skill"),
            "title": clean_text(vid.get("title")),
            "description": clean_text(vid.get("description"))
        }
        cleaned_videos.append(cleaned_video)

    with open("data/youtube_cleaned.json", "w") as f:
        json.dump(cleaned_videos, f, indent=4)

    print("✅ YouTube data cleaned!")


# -------- RUN --------
if __name__ == "__main__":
    clean_jobs()
    clean_youtube()