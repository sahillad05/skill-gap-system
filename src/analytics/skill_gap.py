from sqlalchemy.orm import sessionmaker
from database.db import engine
from src.database.models import Job, YouTube
from collections import Counter

Session = sessionmaker(bind=engine)
session = Session()


# -------- FETCH DATA --------
jobs = session.query(Job).all()
videos = session.query(YouTube).all()


# -------- DEMAND CALCULATION --------
job_skills = []

for job in jobs:
    if job.skills:
        job_skills.extend(job.skills.split(","))

demand_counter = Counter(job_skills)


# -------- SUPPLY CALCULATION --------
video_skills = []

for vid in videos:
    if vid.skills:
        video_skills.extend(vid.skills.split(","))

supply_counter = Counter(video_skills)


# -------- SKILL GAP CALCULATION --------
all_skills = set(demand_counter.keys()).union(set(supply_counter.keys()))

results = []

for skill in all_skills:
    demand = demand_counter.get(skill, 0)
    supply = supply_counter.get(skill, 0)

    gap = (demand * 0.6) - (supply * 0.4)

    results.append({
        "skill": skill,
        "demand": demand,
        "supply": supply,
        "gap": round(gap, 2)
    })


# -------- SORT BY GAP --------
results = sorted(results, key=lambda x: x["gap"], reverse=True)


# -------- PRINT TOP SKILLS --------
print("\n🔥 Top Skill Gaps:\n")

for r in results[:10]:
    print(r)


import json

with open("data/skill_gap_results.json", "w") as f:
    json.dump(results, f, indent=4)

print("✅ Results saved!")