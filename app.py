import streamlit as st
import plotly.graph_objects as go

# Streamlit config
st.set_page_config(page_title="NeuroGuard Flow & Ethics", layout="wide", initial_sidebar_state="collapsed")

# Dark theme CSS
st.markdown("""
    <style>
    body, .stApp {
        background-color: #0d1117;
        color: #e6edf3;
    }
    h1, h2, h3 {
        color: #58a6ff;
    }
    .css-18ni7ap {
        background-color: #0d1117;
    }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown("<h1 style='text-align: center;'>⚙️ NeuroGuard Therapeutic Architecture & Ethics Radar</h1>", unsafe_allow_html=True)
st.markdown("---")

# FLOWCHART SECTION
st.subheader("🧬 Adaptive Multimodal Neuro-Oncological Protocol (AMNP): Full-Stack Therapeutic Cascade")

flow_fig = go.Figure()
steps = ["Diagnosis (MRI + Organoids)", 
         "Mutation Prediction (Quantum AI)", 
         "Multimodal Attack (Nanobots + CRISPR)", 
         "Neural Regeneration (3D Bioprinting)", 
         "Real-Time Surveillance (Implants + AI)"]
x_pos = [0.1, 0.3, 0.5, 0.7, 0.9]
colors = ['#1f77b4', '#17becf', '#d62728', '#2ca02c', '#ff7f0e']

for i, step in enumerate(steps):
    flow_fig.add_shape(type="rect", x0=x_pos[i]-0.08, y0=0.4, x1=x_pos[i]+0.08, y1=0.6,
                       line=dict(color='white'), fillcolor=colors[i])
    flow_fig.add_annotation(x=x_pos[i], y=0.5, text=f"<b>{step}</b>", showarrow=False,
                            font=dict(size=13, color='white'))

for i in range(len(steps)-1):
    flow_fig.add_annotation(x=x_pos[i]+0.09, y=0.5, ax=x_pos[i+1]-0.09, ay=0.5,
                            showarrow=True, arrowhead=2, arrowsize=2, arrowwidth=2, arrowcolor="white")

flow_fig.update_layout(
    xaxis=dict(visible=False), yaxis=dict(visible=False),
    template="plotly_dark", height=330,
    margin=dict(l=20, r=20, t=30, b=20),
    plot_bgcolor='#0d1117', paper_bgcolor='#0d1117'
)

st.plotly_chart(flow_fig, use_container_width=True)

# ETHICAL COMPARISON RADAR
st.subheader("⚖️ Comparative Ethical Impact Radar")

variables = ['Risk', 'Autonomy', 'Reversibility', 'Precision', 'Regeneration']
traditional = [70, 30, 20, 45, 10]
neuroguard = [15, 90, 85, 95, 95]

radar_fig = go.Figure()
radar_fig.add_trace(go.Scatterpolar(r=traditional, theta=variables, fill='toself',
                                    name='Traditional Therapies', line_color='#ff4c4c'))
radar_fig.add_trace(go.Scatterpolar(r=neuroguard, theta=variables, fill='toself',
                                    name='NeuroGuard System', line_color='#00ccff'))

radar_fig.update_layout(
    polar=dict(
        bgcolor='#0d1117',
        radialaxis=dict(visible=True, range=[0, 100], gridcolor='gray', linecolor='gray'),
        angularaxis=dict(tickfont=dict(color='white'))
    ),
    template='plotly_dark',
    showlegend=True,
    height=550,
    legend=dict(font=dict(size=12)),
    title="Ethical and Functional Comparison: Traditional vs NeuroGuard"
)

st.plotly_chart(radar_fig, use_container_width=True)
