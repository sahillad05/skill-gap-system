# 🚀 Real-Time Skill Gap Intelligence System

## 🌐 Live Demo

👉 https://your-render-app.onrender.com

---

## 📌 Overview

The **Real-Time Skill Gap Intelligence System** is an end-to-end data product that identifies the gap between **job market demand** and **learning supply**, helping users discover the most valuable skills to learn.

This system integrates real-time APIs, processes unstructured data, performs dynamic analytics, and visualizes insights through an interactive dashboard.

---

## 🎯 Problem Statement

In today’s fast-changing job market, learners struggle to answer:

* Which skills are currently in demand?
* Which skills are oversaturated?
* What should I learn next?

---

## 💡 Solution

This system provides:

* 📊 Demand analysis from job postings
* 📉 Supply analysis from learning content
* 🚀 Skill gap scoring to identify high-opportunity skills

---

## 🏗️ System Architecture

┌──────────────┐     ┌────────────────┐
│  Adzuna API  │     │  YouTube API   │
└──────┬───────┘     └───────┬────────┘
       │                     │
       └────────┬────────────┘
                ▼
       ┌────────────────┐
       │ Data Ingestion │
       └───────┬────────┘
               ▼
       ┌────────────────┐
       │ Data Cleaning  │
       └───────┬────────┘
               ▼
       ┌──────────────────┐
       │ Skill Extraction │  ← NLP / Dictionary Matching
       └───────┬──────────┘
               ▼
       ┌────────────────┐
       │  Supabase DB   │  ← PostgreSQL
       └───────┬────────┘
               ▼
       ┌──────────────────┐
       │ Analytics Engine │  ← Gap Score Calculation
       └───────┬──────────┘
               ▼
       ┌────────────────┐
       │  Streamlit UI  │  ← Interactive Dashboard
       └────────────────┘

---

## ⚙️ Tech Stack

* **Language:** Python
* **Backend:** SQLAlchemy
* **Frontend:** Streamlit, Plotly
* **Database:** Supabase (PostgreSQL)
* **APIs:** Adzuna API, YouTube Data API
* **Automation:** GitHub Actions (CI/CD)
* **Deployment:** Render

---

## 🔌 Data Sources

### 🟢 Job Data

* Source: Adzuna API
* Fields: Title, Location, Salary, Description

### 🔵 Learning Data

* Source: YouTube API
* Fields: Title, Description

---

## 🧠 Core Features

### 🔹 Skill Extraction

* NLP-based keyword matching
* Converts raw text → structured skill list

---

### 🔹 Demand vs Supply Analysis

* Demand = Frequency in job postings
* Supply = Frequency in tutorials

---

### 🔹 Skill Gap Formula

```
Gap Score = (Demand × 0.6) − (Supply × 0.4)
```

---

### 🔹 Dynamic Filtering (🔥 Advanced Feature)

* Filter by **Location**
* Filter by **Role (Data Analyst, ML Engineer, etc.)**
* Real-time recomputation of metrics

---

### 🔹 Time-Series Analysis

* Tracks job trends over time
* Uses timestamped job data
* Visualized using line charts

---

### 🔹 Interactive Dashboard

* 📊 KPI Metrics
* 🔥 Gap Leaderboard
* 📈 Demand vs Supply Chart
* 🎯 Quadrant Analysis
* 📡 Radar Comparison
* 📅 Time-Series Trends
* 📋 Styled Data Table

---

## ⚡ Automation

* Daily pipeline using **GitHub Actions**
* Fetch → Process → Store → Analyze → Update

---

## 🗄️ Database Schema

### Table: jobs

* id
* title
* location
* salary
* skills
* created_at

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

| Component  | Platform       |
| ---------- | -------------- |
| Dashboard  | Render         |
| Database   | Supabase       |
| Automation | GitHub Actions |

---

## ▶️ Run Locally

```bash
git clone https://github.com/sahillad05/skill-gap-system.git
cd skill-gap-system

# Create virtual environment
python -m venv venv
venv\Scripts\activate   # Windows

# Install dependencies
pip install -r requirements.txt

# Run pipeline
python -m src.ingestion.adzuna_jobs
python -m src.processing.clean_data
python -m src.processing.skill_extraction
python -m src.database.insert_data
python -m src.analytics.skill_gap

# Run dashboard
python -m streamlit run src/dashboard/app.py
```

---

## 🧠 Key Learnings

* End-to-end data pipeline design
* API integration and data ingestion
* Dynamic analytics with real-time filtering
* Cloud database (Supabase) integration
* CI/CD automation using GitHub Actions
* Dashboard design and UI optimization

---


## 🔮 Future Improvements

* Add ML-based skill extraction
* Integrate LinkedIn / Indeed APIs
* Add user personalization
* Real-time streaming pipeline (Kafka)
* Recommendation engine

---

## 👨‍💻 Author

**Sahil Lad**
MSc Data Science

---

## ⭐ If you found this useful

Give this repo a ⭐ on GitHub!
