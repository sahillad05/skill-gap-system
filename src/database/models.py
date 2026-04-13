from sqlalchemy import Column, Integer, String, Text, Float
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


class YouTube(Base):
    __tablename__ = "youtube"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(Text)
    skills = Column(Text)