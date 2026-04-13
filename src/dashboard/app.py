import streamlit as st
import json
import pandas as pd

st.set_page_config(page_title="Skill Gap Intelligence System", layout="wide")

st.title("🚀 Real-Time Skill Gap Intelligence Dashboard")

# -------- LOAD DATA --------
with open("data/skill_gap_results.json", "r") as f:
    data = json.load(f)

df = pd.DataFrame(data)

# -------- OVERVIEW --------
st.subheader("📊 Overview")

col1, col2, col3 = st.columns(3)

col1.metric("Total Skills", len(df))
col2.metric("Avg Demand", int(df["demand"].mean()))
col3.metric("Avg Supply", int(df["supply"].mean()))

# -------- TOP SKILLS --------
st.subheader("🔥 Top Skills to Learn")

top_skills = df.sort_values(by="gap", ascending=False).head(10)

st.bar_chart(top_skills.set_index("skill")["gap"])

# -------- SUPPLY VS DEMAND --------
st.subheader("⚖️ Demand vs Supply")

selected_skills = st.multiselect(
    "Select Skills",
    df["skill"].tolist(),
    default=df["skill"].tolist()[:5]
)

filtered_df = df[df["skill"].isin(selected_skills)]

st.line_chart(filtered_df.set_index("skill")[["demand", "supply"]])

# -------- TABLE --------
st.subheader("📋 Full Skill Data")

st.dataframe(df)