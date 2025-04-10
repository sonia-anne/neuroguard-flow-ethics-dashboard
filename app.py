import streamlit as st
import plotly.graph_objects as go

# Page config
st.set_page_config(page_title="NeuroGuard Pipeline & Ethical Radar", layout="wide")

# Dark theme styling
st.markdown("""
    <style>
    body, .stApp {
        background-color: #0d1117;
        color: #e6edf3;
    }
    h1, h2, h3 {
        color: #58a6ff;
    }
    .block-container {
        padding: 2rem;
    }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown("<h1 style='text-align: center;'>NeuroGuard Operational Framework & Bioethics Matrix</h1>", unsafe_allow_html=True)
st.markdown("---")

# FLOWCHART
st.subheader("🧠 Precision Cascade for Glioblastoma Intervention")

fig_flow = go.Figure()

steps = [
    "1. Smart Diagnosis:\nMRI + AI-based GBM classifier",
    "2. Genomic Prediction:\nQuantum neural networks simulate tumor evolution",
    "3. Adaptive Attack:\nNanobots + Virus + CRISPR payload delivery",
    "4. Regenerative Layer:\n3D bioprinting + Neurotrophic infusion",
    "5. Sentinel Monitoring:\nBiodegradable implants + real-time alerts"
]

y_positions = [1, 0.8, 0.6, 0.4, 0.2]
colors = ['#58a6ff', '#17becf', '#d62728', '#2ca02c', '#ffb347']

for i, step in enumerate(steps):
    fig_flow.add_shape(type="rect",
                       x0=0.25, y0=y_positions[i] - 0.05,
                       x1=0.75, y1=y_positions[i] + 0.05,
                       line=dict(color="white"),
                       fillcolor=colors[i])
    fig_flow.add_annotation(x=0.5, y=y_positions[i],
                            text=f"<b>{step}</b>",
                            showarrow=False,
                            font=dict(size=13, color="white"))

for i in range(len(steps)-1):
    fig_flow.add_annotation(
        x=0.5, y=y_positions[i] - 0.06,
        ax=0.5, ay=y_positions[i+1] + 0.06,
        showarrow=True,
        arrowhead=3,
        arrowsize=2,
        arrowwidth=2,
        arrowcolor="white"
    )

fig_flow.update_layout(
    height=600,
    xaxis=dict(visible=False),
    yaxis=dict(visible=False),
    margin=dict(t=30, b=30, l=20, r=20),
    template="plotly_dark",
    plot_bgcolor="#0d1117",
    paper_bgcolor="#0d1117"
)

st.plotly_chart(fig_flow, use_container_width=True)

# ETHICS RADAR
st.subheader("⚖️ Ethical Metrics: NeuroGuard vs Conventional Approaches")

labels = ['Patient Risk', 'Autonomy', 'Reversibility', 'Therapeutic Precision', 'Functional Recovery']
traditional_scores = [70, 40, 30, 55, 15]
neuroguard_scores = [20, 90, 85, 98, 92]

radar_fig = go.Figure()

radar_fig.add_trace(go.Scatterpolar(
    r=traditional_scores,
    theta=labels,
    fill='toself',
    name='Conventional',
    line_color='#ff4c4c'
))

radar_fig.add_trace(go.Scatterpolar(
    r=neuroguard_scores,
    theta=labels,
    fill='toself',
    name='NeuroGuard',
    line_color='#00ccff'
))

radar_fig.update_layout(
    polar=dict(
        bgcolor="#0d1117",
        radialaxis=dict(visible=True, range=[0, 100], gridcolor='gray', linecolor='gray'),
        angularaxis=dict(tickfont=dict(color='white'))
    ),
    template="plotly_dark",
    height=550,
    title="Bioethical Comparative Matrix: NeuroGuard vs Standard Protocols"
)

st.plotly_chart(radar_fig, use_container_width=True)
