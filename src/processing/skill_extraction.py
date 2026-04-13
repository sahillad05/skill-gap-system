import json

# -------- SKILL DICTIONARY --------
SKILLS = [
    "python", "sql", "machine learning", "deep learning",
    "nlp", "power bi", "tableau", "excel",
    "data analysis", "pandas", "numpy"
]


# -------- SKILL EXTRACTION FUNCTION --------
def extract_skills(text):
    found_skills = []

    for skill in SKILLS:
        if skill in text:
            found_skills.append(skill)

    return list(set(found_skills))


# -------- PROCESS JOB DATA --------
def process_jobs():
    with open("data/jobs_cleaned.json", "r") as f:
        jobs = json.load(f)

    for job in jobs:
        combined_text = job["title"] + " " + job["description"]
        job["skills"] = extract_skills(combined_text)

    with open("data/jobs_with_skills.json", "w") as f:
        json.dump(jobs, f, indent=4)

    print("✅ Skills extracted from jobs!")


# -------- PROCESS YOUTUBE DATA --------
def process_youtube():
    with open("data/youtube_cleaned.json", "r") as f:
        videos = json.load(f)

    for vid in videos:
        combined_text = vid["title"] + " " + vid["description"]
        vid["skills"] = extract_skills(combined_text)

    with open("data/youtube_with_skills.json", "w") as f:
        json.dump(videos, f, indent=4)

    print("✅ Skills extracted from YouTube!")


# -------- RUN --------
if __name__ == "__main__":
    process_jobs()
    process_youtube()