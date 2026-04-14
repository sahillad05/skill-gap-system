# 🚀 Real-Time Skill Gap Intelligence System

## 📌 Overview

The **Real-Time Skill Gap Intelligence System** is a production-ready data analytics platform that analyzes the gap between **job market demand** and **learning supply** to identify the most valuable skills to learn.

It integrates real-time job postings and learning content, processes unstructured text using NLP techniques, and presents insights through an interactive dashboard.

---

## 🎯 Problem Statement

Learners often struggle to identify:

* Which skills are currently in demand
* Which skills are oversaturated
* What to learn next for maximum career growth

---

## 💡 Solution

This system answers:

* 📊 Which skills are most demanded in the job market?
* 📉 Which skills are oversaturated?
* 🚀 Which skills have the highest opportunity (skill gap)?

Using:

* Job data (Adzuna API)
* Learning data (YouTube API)
* Analytics engine (Demand vs Supply)

---

## 🏗️ System Architecture

```
          ┌──────────────┐
          │ Adzuna API   │
          └──────┬───────┘
                 │
          ┌──────▼───────┐
          │ Data Ingestion│
          └──────┬───────┘
                 │
          ┌──────▼────────┐
          │ Data Cleaning │
          └──────┬────────┘
                 │
          ┌──────▼────────┐
          │ Skill Extraction│
          └──────┬────────┘
                 │
          ┌──────▼────────┐
          │ Supabase DB   │
          └──────┬────────┘
                 │
          ┌──────▼────────┐
          │ Analytics Engine│
          └──────┬────────┘
                 │
          ┌──────▼────────┐
          │ Streamlit UI  │
          └───────────────┘
```

---

## ⚙️ Tech Stack

* **Languages**: Python
* **Libraries**: Pandas, NumPy, SQLAlchemy, Streamlit, Plotly
* **APIs**: Adzuna API, YouTube Data API
* **Database**: Supabase (PostgreSQL)
* **Automation**: GitHub Actions (CI/CD pipeline)
* **Deployment**: Render

---

## 🔌 Data Sources

### 🟢 Job Data

* Source: Adzuna API
* Fields: Title, Description, Location, Salary

### 🔵 Learning Data

* Source: YouTube Data API
* Fields: Title, Description

---

## 🧠 Core Features

### 🔹 1. Skill Extraction (NLP)

* Dictionary-based skill matching
* Converts raw text → structured skill lists

### 🔹 2. Demand Calculation

* Counts skill occurrences in job postings

### 🔹 3. Supply Calculation

* Counts skill occurrences in learning content

### 🔹 4. Skill Gap Score

```
Weighted Gap = (Demand × 0.6) − (Supply × 0.4)
```

* High score → High opportunity
* Low/negative → Saturated skill

---

## 📊 Dashboard Features

* 📌 Skill Gap Leaderboard
* 📊 Demand vs Supply Comparison
* 📉 Gap Score Visualization
* 🧭 Quadrant Analysis (Demand vs Supply)
* 📡 Radar Comparison
* 📋 Interactive Data Table

---

## ⚡ Automation

* Daily pipeline execution using **GitHub Actions**
* Fetch → Process → Store → Analyze → Update dashboard
* Runs independently of local system

---

## 🗄️ Database Schema

### Table: jobs

* id
* title
* description
* location
* salary
* skills

### Table: youtube

* id
* title
* description
* skills

### Table: skill_metrics

* skill
* demand_count
* supply_count
* weighted_gap_score

---

## 🚀 Deployment

* **Dashboard**: Render
* **Database**: Supabase
* **Automation**: GitHub Actions

---

## ▶️ How to Run Locally

```bash
# Clone repo
git clone https://github.com/sahillad05/skill-gap-system.git
cd skill-gap-system

# Create environment
python -m venv venv
venv\Scripts\activate   # Windows

# Install dependencies
pip install -r requirements.txt

# Run pipeline
python -m src.ingestion.adzuna_jobs
python -m src.ingestion.youtube_data
python -m src.processing.clean_data
python -m src.processing.skill_extraction
python -m src.database.insert_data
python -m src.analytics.skill_gap

# Run dashboard
streamlit run src/dashboard/app.py
```

---

## 🌐 Live Demo

👉 [https://skill-gap-system.onrender.com]

---

## 🧠 Key Learnings

* End-to-end data pipeline design
* API integration and data ingestion
* NLP-based feature extraction
* Cloud database (Supabase) integration
* CI/CD automation with GitHub Actions
* Dashboard development with Streamlit

---

## 🔮 Future Improvements

* Add time-series trend analysis
* Improve skill extraction using ML/NLP models
* Add user personalization (role-based recommendations)
* Integrate more job platforms (LinkedIn, Indeed)

---

## 👨‍💻 Author

**Sahil Lad**
MSc Data Science

---

## ⭐ If you found this useful

Give this repo a ⭐ on GitHub!
