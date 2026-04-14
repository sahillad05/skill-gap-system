from sqlalchemy import Column, Integer, String, Text, Float, DateTime
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Job(Base):
    __tablename__ = "jobs"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(Text)
    location = Column(String)
    salary = Column(Float)
    skills = Column(Text)  # store as comma-separated
    created_at = Column(DateTime)


class YouTube(Base):
    __tablename__ = "youtube"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(Text)
    skills = Column(Text)


class SkillMetrics(Base):
    __tablename__ = "skill_metrics"

    skill = Column(String, primary_key=True)
    demand_count = Column(Integer)
    supply_count = Column(Integer)
    weighted_gap_score = Column(Float)