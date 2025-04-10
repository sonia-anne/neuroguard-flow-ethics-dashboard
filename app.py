import streamlit as st
import plotly.graph_objects as go

st.set_page_config(page_title="NeuroGuard Timeline & Ethics", layout="wide", initial_sidebar_state="collapsed")

st.markdown("""
    <style>
    body, .stApp {
        background-color: #0d1117;
        color: #e6edf3;
    }
    h1, h2, h3 {
        color: #58a6ff;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center;'>📊 NeuroGuard Evolution Pipeline & Ethics Comparison</h1>", unsafe_allow_html=True)
st.markdown("---")

# TIMELINE STYLE BAR CHART
st.subheader("🚀 Adaptive Neuro-Oncology Timeline")

phases = [
    "Diagnosis Phase",
    "Mutation Prediction (AI + Quantum)",
    "Multimodal Attack (Nanotech)",
    "Neural Regeneration (3D)",
    "Smart Surveillance (IA + BioSensors)"
]

descriptions = [
    "Organoids + MRI mapped by AI to detect GBM.",
    "Quantum-based evolution simulations to forecast tumor mutations.",
    "Nanobots + CRISPR + Oncolytic viruses targeting tumor at genetic and structural level.",
    "3D Bioprinting of scaffolded neural tissue guided by functional data.",
    "Embedded smart implants monitor recurrence and adapt treatment in real time."
]

scores = [1, 2, 3, 4, 5]

fig_bar = go.Figure()

fig_bar.add_trace(go.Bar(
    x=scores,
    y=phases,
    orientation='h',
    text=descriptions,
    textposition='auto',
    marker=dict(
        color=['#1f77b4', '#00ccff', '#d62728', '#2ca02c', '#ff7f0e'],
        line=dict(color='white', width=1.5)
    )
))

fig_bar.update_layout(
    title="Therapeutic Cascade of NeuroGuard (Pipeline Overview)",
    xaxis_title='Progression (1 = Initial Phase, 5 = Advanced)',
    yaxis_title='',
    yaxis=dict(autorange="reversed"),
    template='plotly_dark',
    height=600
)

st.plotly_chart(fig_bar, use_container_width=True)

# RADAR CHART – ETHICAL IMPACT
st.subheader("⚖️ Comparative Ethical Impact Radar")

criteria = ['Risk', 'Autonomy', 'Reversibility', 'Precision', 'Regeneration']
traditional = [70, 30, 20, 45, 10]
neuroguard = [15, 90, 85, 95, 95]

fig_radar = go.Figure()
fig_radar.add_trace(go.Scatterpolar(r=traditional, theta=criteria, fill='toself',
                                    name='Traditional Therapies', line_color='#ff4c4c'))
fig_radar.add_trace(go.Scatterpolar(r=neuroguard, theta=criteria, fill='toself',
                                    name='NeuroGuard System', line_color='#00ccff'))

fig_radar.update_layout(
    polar=dict(
        bgcolor='#0d1117',
        radialaxis=dict(visible=True, range=[0, 100], gridcolor='gray', linecolor='gray'),
        angularaxis=dict(tickfont=dict(color='white'))
    ),
    template='plotly_dark',
    height=550,
    title="Ethical Comparison: Traditional vs. NeuroGuard",
    showlegend=True
)

st.plotly_chart(fig_radar, use_container_width=True)