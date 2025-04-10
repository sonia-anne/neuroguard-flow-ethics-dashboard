import streamlit as st
import plotly.express as px
import pandas as pd

# Page configuration
st.set_page_config(page_title="NeuroGuard Advanced Timeline", layout="wide", initial_sidebar_state="collapsed")

# Dark theme CSS
st.markdown("""
    <style>
    body, .stApp {
        background-color: #0d1117;
        color: #e6edf3;
    }
    .css-18ni7ap {
        background-color: #0d1117;
    }
    h1, h2, h3 {
        color: #58a6ff;
    }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown("<h1 style='text-align: center;'>🧬 NeuroGuard Global Deployment Timeline</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center;'>From Organoid Simulation to Mars: The Next Decade of Neuro-Oncology</h3>", unsafe_allow_html=True)
st.markdown("---")

# Timeline data
timeline_data = pd.DataFrame({
    'Milestone': [
        "Organoid Simulation Phase", 
        "Preclinical Trials in Animals", 
        "Human Ethics Approval & Testing", 
        "Nanobot-CRISPR Integration", 
        "NeuroRegenerative Bioprinting", 
        "AI + Quantum Prediction Modules", 
        "FDA Global Authorization", 
        "Space NeuroGuard: Mars Deployment"
    ],
    'Year': [2025, 2027, 2028, 2029, 2030, 2031, 2033, 2035],
    'Details': [
        "Use of human-derived cerebral organoids to test AI nanobot targeting precision.",
        "Implementation of full system in rodents and primates with real-time neural monitoring.",
        "Approval of terminal-phase GBM human trial protocols with embedded safety failsafes.",
        "Fusion of CRISPR-Cas13d genetic silencing into nanobot delivery systems.",
        "Intracranial 3D bioprinting of neurons in affected zones after tumor removal.",
        "Deployment of quantum AI to anticipate tumor evolution and therapy resistance.",
        "World-scale rollout of NeuroGuard following multi-agency clinical validation.",
        "Testing of autonomous neural regeneration in microgravity (SpaceX & NASA partnership)."
    ],
    'Color': ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#17becf', '#8c564b', '#e377c2']
})

# Build interactive timeline
fig = px.timeline(
    timeline_data, 
    x_start='Year', 
    x_end=[y + 0.5 for y in timeline_data['Year']], 
    y='Milestone', 
    color='Milestone', 
    color_discrete_sequence=timeline_data['Color'],
    hover_name='Milestone',
    hover_data={'Year': True, 'Details': True}
)

fig.update_yaxes(autorange="reversed")
fig.update_layout(
    template='plotly_dark',
    title="NeuroGuard Deployment Timeline (2025–2035+)",
    xaxis_title="Year",
    yaxis_title="Milestones",
    height=600,
    showlegend=False
)

st.plotly_chart(fig, use_container_width=True)