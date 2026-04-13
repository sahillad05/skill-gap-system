import json
from db import engine
from models import Job, YouTube
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
session = Session()


# -------- INSERT JOBS --------
with open("data/jobs_with_skills.json", "r") as f:
    jobs = json.load(f)

for job in jobs:
    new_job = Job(
        title=job["title"],
        description=job["description"],
        location=job["location"],
        salary=job["salary"],
        skills=",".join(job["skills"])
    )
    session.add(new_job)


# -------- INSERT YOUTUBE --------
with open("data/youtube_with_skills.json", "r") as f:
    videos = json.load(f)

for vid in videos:
    new_vid = YouTube(
        title=vid["title"],
        description=vid["description"],
        skills=",".join(vid["skills"])
    )
    session.add(new_vid)


session.commit()
print("✅ Data inserted into database!")