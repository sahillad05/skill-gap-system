import streamlit as st
import json
import pandas as pd
import plotly.graph_objects as go
from datetime import datetime

# ── Page config ───────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Skill Gap Intelligence",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ── Minimal CSS ───────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;600&display=swap');

.block-container { padding-top: 1.5rem; padding-bottom: 2rem; }

[data-testid="stMetricLabel"] p {
    font-size: 11px !important;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    color: #64748b !important;
    font-weight: 600;
}
[data-testid="stMetricValue"] {
    font-family: 'IBM Plex Mono', monospace !important;
    font-size: 28px !important;
    font-weight: 600 !important;
}

.section-header {
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    color: #475569;
    padding-bottom: 8px;
    border-bottom: 1px solid rgba(100,116,139,0.2);
    margin-bottom: 16px;
    font-family: 'IBM Plex Mono', monospace;
}

.lb-wrap { margin-top: 4px; }
.lb-row {
    display: flex;
    align-items: center;
    padding: 10px 14px;
    border-radius: 6px;
    margin-bottom: 6px;
    background: rgba(100,116,139,0.06);
    border: 1px solid rgba(100,116,139,0.12);
    gap: 12px;
}
.lb-rank {
    font-family: 'IBM Plex Mono', monospace;
    font-size: 11px;
    color: #64748b;
    width: 24px;
    flex-shrink: 0;
}
.lb-skill { flex: 1; font-size: 13px; font-weight: 500; }
.lb-pill {
    font-size: 10px;
    font-weight: 700;
    font-family: 'IBM Plex Mono', monospace;
    letter-spacing: 0.06em;
    padding: 2px 8px;
    border-radius: 4px;
}
.pill-hot  { background: rgba(239,68,68,0.12);  color: #ef4444; }
.pill-good { background: rgba(16,185,129,0.12); color: #10b981; }
.pill-mid  { background: rgba(245,158,11,0.12); color: #f59e0b; }
.lb-score {
    font-family: 'IBM Plex Mono', monospace;
    font-size: 13px;
    font-weight: 600;
    width: 48px;
    text-align: right;
}
</style>
""", unsafe_allow_html=True)


# ── Colors & helpers ──────────────────────────────────────────────────────────
C_BLUE, C_TEAL, C_AMBER, C_RED, C_GREEN, C_PURPLE = (
    "#3b82f6", "#14b8a6", "#f59e0b", "#ef4444", "#10b981", "#8b5cf6"
)

def gap_color(v):
    if v >= 80: return C_RED
    if v >= 40: return C_GREEN
    return C_AMBER

# Base layout: NO legend key here — prevents duplicate kwarg crash
def base_layout(**overrides):
    layout = dict(
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font=dict(family="Inter, sans-serif", size=12, color="#94a3b8"),
        margin=dict(l=12, r=12, t=36, b=12),
        xaxis=dict(
            gridcolor="rgba(100,116,139,0.15)",
            zerolinecolor="rgba(100,116,139,0.2)",
            tickfont=dict(size=11),
            linecolor="rgba(100,116,139,0.2)",
        ),
        yaxis=dict(
            gridcolor="rgba(100,116,139,0.15)",
            zerolinecolor="rgba(100,116,139,0.2)",
            tickfont=dict(size=11),
            linecolor="rgba(100,116,139,0.2)",
        ),
    )
    layout.update(overrides)
    return layout


# ── Load data ─────────────────────────────────────────────────────────────────
@st.cache_data(ttl=300)
def load_data():
    try:
        with open("data/skill_gap_results.json") as f:
            return pd.DataFrame(json.load(f))
    except FileNotFoundError:
        return pd.DataFrame([
            {"skill": "Python",           "demand": 320, "supply": 180},
            {"skill": "SQL",              "demand": 290, "supply": 200},
            {"skill": "Machine Learning", "demand": 250, "supply": 110},
            {"skill": "Power BI",         "demand": 210, "supply": 90},
            {"skill": "Tableau",          "demand": 190, "supply": 140},
            {"skill": "Deep Learning",    "demand": 160, "supply": 80},
            {"skill": "NLP",              "demand": 140, "supply": 60},
            {"skill": "Docker",           "demand": 130, "supply": 95},
            {"skill": "Spark",            "demand": 110, "supply": 50},
            {"skill": "Airflow",          "demand": 100, "supply": 40},
            {"skill": "Excel",            "demand": 170, "supply": 300},
            {"skill": "Kubernetes",       "demand": 95,  "supply": 70},
        ])

df = load_data()
if "gap" not in df.columns:
    df["gap"] = (df["demand"] * 0.6) - (df["supply"] * 0.4)
df["gap"] = df["gap"].round(1)


# ── Sidebar ───────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("### Filters")
    top_n = st.slider("Skills to show", 5, len(df), 10)
    show_negative = st.checkbox("Include oversaturated skills", value=False)
    sort_by = st.radio("Sort by", ["Gap Score", "Demand", "Supply"])
    st.divider()
    st.caption(f"Last refresh  \n{datetime.now().strftime('%d %b %Y  %H:%M')}")
    st.caption("**Gap formula**  \n`(Demand × 0.6) − (Supply × 0.4)`")


# ── Filter ────────────────────────────────────────────────────────────────────
sort_col = {"Gap Score": "gap", "Demand": "demand", "Supply": "supply"}[sort_by]
df_sorted = df.sort_values(sort_col, ascending=False)
if not show_negative:
    df_sorted = df_sorted[df_sorted["gap"] >= 0]
df_top = df_sorted.head(top_n).reset_index(drop=True)


# ── Header ────────────────────────────────────────────────────────────────────
st.markdown("## Skill Gap Intelligence")
st.caption("Job market demand vs. learning supply · updated weekly")
st.divider()


# ── KPI row ───────────────────────────────────────────────────────────────────
k1, k2, k3, k4 = st.columns(4)
top_skill_row = df.sort_values("gap", ascending=False).iloc[0]
k1.metric("Skills Tracked",    str(len(df)))
k2.metric("Total Job Signals", f"{df['demand'].sum():,}")
k3.metric("Total Tutorials",   f"{df['supply'].sum():,}")
k4.metric("Hottest Skill",     top_skill_row["skill"],
          f"gap score {top_skill_row['gap']:.0f}")

st.markdown("<br>", unsafe_allow_html=True)


# ── Row 1: Leaderboard + Grouped bar ─────────────────────────────────────────
col_lb, col_bar = st.columns([1, 1.7], gap="large")

with col_lb:
    st.markdown('<p class="section-header">Gap Leaderboard</p>', unsafe_allow_html=True)
    html = '<div class="lb-wrap">'
    for i, row in df_top.iterrows():
        g = row["gap"]
        pill_cls = "pill-hot" if g >= 80 else ("pill-good" if g >= 40 else "pill-mid")
        pill_lbl = "HOT"      if g >= 80 else ("LEARN"     if g >= 40 else "WATCH")
        sc       = C_RED      if g >= 80 else (C_GREEN      if g >= 40 else C_AMBER)
        html += f"""
        <div class="lb-row">
          <span class="lb-rank">#{i+1:02d}</span>
          <span class="lb-skill">{row['skill']}</span>
          <span class="lb-pill {pill_cls}">{pill_lbl}</span>
          <span class="lb-score" style="color:{sc}">{g}</span>
        </div>"""
    html += "</div>"
    st.markdown(html, unsafe_allow_html=True)

with col_bar:
    st.markdown('<p class="section-header">Demand vs Supply</p>', unsafe_allow_html=True)
    fig_bar = go.Figure()
    fig_bar.add_trace(go.Bar(
        name="Demand", x=df_top["skill"], y=df_top["demand"],
        marker_color=C_BLUE, marker_line_width=0,
    ))
    fig_bar.add_trace(go.Bar(
        name="Supply", x=df_top["skill"], y=df_top["supply"],
        marker_color=C_TEAL, marker_line_width=0,
    ))
    fig_bar.update_layout(**base_layout(
        barmode="group",
        bargap=0.3,
        bargroupgap=0.08,
        height=380,
        legend=dict(                         # legend defined HERE only, not in base_layout
            orientation="h",
            yanchor="bottom", y=1.02,
            xanchor="right",  x=1,
            bgcolor="rgba(0,0,0,0)",
            font=dict(size=11, color="#94a3b8"),
        ),
    ))
    st.plotly_chart(fig_bar, use_container_width=True)


st.markdown("<br>", unsafe_allow_html=True)


# ── Row 2: Horizontal gap bar + Scatter ──────────────────────────────────────
col_gap, col_sc = st.columns(2, gap="large")

with col_gap:
    st.markdown('<p class="section-header">Weighted Gap Score</p>', unsafe_allow_html=True)
    fig_h = go.Figure(go.Bar(
        x=df_top["gap"],
        y=df_top["skill"],
        orientation="h",
        marker_color=[gap_color(v) for v in df_top["gap"]],
        marker_line_width=0,
        text=df_top["gap"],
        textposition="outside",
        textfont=dict(size=11, color="#94a3b8"),
    ))
    fig_h.update_layout(**base_layout(
        height=360,
        showlegend=False,
        yaxis=dict(
            autorange="reversed",
            gridcolor="rgba(100,116,139,0.15)",
            tickfont=dict(size=11),
        ),
    ))
    st.plotly_chart(fig_h, use_container_width=True)

with col_sc:
    st.markdown('<p class="section-header">Demand / Supply Quadrant</p>', unsafe_allow_html=True)
    mx = max(df_top["demand"].max(), df_top["supply"].max()) * 1.15
    fig_sc = go.Figure()
    fig_sc.add_shape(
        type="line", x0=0, y0=0, x1=mx, y1=mx,
        line=dict(color="rgba(100,116,139,0.25)", width=1.5, dash="dot"),
    )
    fig_sc.add_annotation(
        x=mx * 0.75, y=mx * 0.83,
        text="supply = demand",
        showarrow=False,
        font=dict(size=10, color="rgba(100,116,139,0.45)"),
    )
    sizes = (df_top["gap"].clip(lower=5) / df_top["gap"].max() * 38 + 8).tolist()
    fig_sc.add_trace(go.Scatter(
        x=df_top["demand"],
        y=df_top["supply"],
        mode="markers+text",
        text=df_top["skill"],
        textposition="top center",
        textfont=dict(size=10, color="#94a3b8"),
        marker=dict(
            size=sizes,
            color=df_top["gap"].tolist(),
            colorscale=[[0, C_AMBER], [0.5, C_BLUE], [1, C_RED]],
            showscale=False,
            line=dict(width=1, color="rgba(0,0,0,0.25)"),
        ),
    ))
    fig_sc.update_layout(**base_layout(
        height=360,
        showlegend=False,
        xaxis=dict(
            title=dict(text="Job Demand", font=dict(size=11, color="#64748b")),
            gridcolor="rgba(100,116,139,0.15)", tickfont=dict(size=11),
        ),
        yaxis=dict(
            title=dict(text="Tutorial Supply", font=dict(size=11, color="#64748b")),
            gridcolor="rgba(100,116,139,0.15)", tickfont=dict(size=11),
        ),
    ))
    st.plotly_chart(fig_sc, use_container_width=True)


st.markdown("<br>", unsafe_allow_html=True)


# ── Radar comparison ─────────────────────────────────────────────────────────
st.markdown('<p class="section-header">Skill Comparison — Radar</p>', unsafe_allow_html=True)

selected = st.multiselect(
    "Select skills to compare",
    options=df["skill"].tolist(),
    default=df["skill"].tolist()[:5],
    label_visibility="collapsed",
)

if selected:
    palette = [C_BLUE, C_TEAL, C_AMBER, C_RED, C_PURPLE, C_GREEN]
    cats    = ["Demand", "Supply", "Gap Score"]
    fig_r   = go.Figure()

    for idx, (_, row) in enumerate(df[df["skill"].isin(selected)].iterrows()):
        c    = palette[idx % len(palette)]
        vals = [row["demand"], row["supply"], max(float(row["gap"]), 0)]
        fig_r.add_trace(go.Scatterpolar(
            r=vals + [vals[0]],
            theta=cats + [cats[0]],
            fill="toself",
            name=row["skill"],
            line=dict(color=c, width=1.5),
        ))

    fig_r.update_layout(
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font=dict(family="Inter, sans-serif", size=12, color="#94a3b8"),
        polar=dict(
            bgcolor="rgba(0,0,0,0)",
            radialaxis=dict(visible=True, gridcolor="rgba(100,116,139,0.2)", color="#64748b"),
            angularaxis=dict(gridcolor="rgba(100,116,139,0.2)", color="#94a3b8"),
        ),
        legend=dict(
            orientation="h",
            yanchor="bottom", y=-0.2,
            xanchor="center", x=0.5,
            bgcolor="rgba(0,0,0,0)",
            font=dict(size=11, color="#94a3b8"),
        ),
        height=380,
        margin=dict(l=40, r=40, t=20, b=60),
    )
    st.plotly_chart(fig_r, use_container_width=True)
else:
    st.info("Select one or more skills to see the radar comparison.", icon="📡")

st.markdown("<br>", unsafe_allow_html=True)


# ── Full data table ───────────────────────────────────────────────────────────
st.markdown('<p class="section-header">Full Dataset</p>', unsafe_allow_html=True)

display_df = (
    df.sort_values("gap", ascending=False)
    .reset_index(drop=True)
    .rename(columns={"skill": "Skill", "demand": "Demand",
                     "supply": "Supply", "gap": "Gap Score"})
)

def _color_gap(v):
    if v >= 80: return f"color: {C_RED};   font-weight: 600"
    if v >= 40: return f"color: {C_GREEN};  font-weight: 600"
    if v >= 0:  return f"color: {C_AMBER}; font-weight: 500"
    return "color: #64748b"

styled = (
    display_df.style
    .applymap(_color_gap, subset=["Gap Score"])
    .background_gradient(subset=["Demand"], cmap="Blues")
    .background_gradient(subset=["Supply"], cmap="YlOrBr")
    .format({"Demand": "{:,}", "Supply": "{:,}", "Gap Score": "{:.1f}"})
)
st.dataframe(styled, use_container_width=True, height=360)


# ── Footer ────────────────────────────────────────────────────────────────────
st.divider()
st.caption(
    "Skill Gap Intelligence System  ·  "
    "Data: Adzuna API + YouTube Data API  ·  "
    "Built with Streamlit & Plotly"
)