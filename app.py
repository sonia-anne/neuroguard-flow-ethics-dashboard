import streamlit as st
import plotly.graph_objects as go

# Page config
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
st.markdown("<h1 style='text-align: center;'>⚙️ NeuroGuard Process Flowchart & Ethics Radar ⚖️</h1>", unsafe_allow_html=True)
st.markdown("---")

# FLOWCHART
st.subheader("🔄 Intelligent Therapeutic Flow: Step-by-Step")

st.markdown("""
<div style='text-align: center; font-size: 16px; margin-bottom: 10px;'>
<b>Diagnosis</b> ➝ <b>Prediction</b> ➝ <b>Attack</b> ➝ <b>Regeneration</b> ➝ <b>Monitoring</b>
</div>
""", unsafe_allow_html=True)

flow_fig = go.Figure()
steps = ["Diagnosis", "Prediction", "Attack", "Regeneration", "Monitoring"]
x_pos = [0.1, 0.3, 0.5, 0.7, 0.9]
colors = ['#1f77b4', '#17becf', '#d62728', '#2ca02c', '#ff7f0e']

for i, step in enumerate(steps):
    flow_fig.add_shape(type="rect", x0=x_pos[i] - 0.08, y0=0.4, x1=x_pos[i] + 0.08, y1=0.6,
                       line=dict(color='white'), fillcolor=colors[i])
    flow_fig.add_annotation(x=x_pos[i], y=0.5, text=f"<b>{step}</b>", showarrow=False,
                            font=dict(size=16, color='white'))

for i in range(len(steps) - 1):
    flow_fig.add_annotation(x=x_pos[i] + 0.09, y=0.5, ax=x_pos[i+1] - 0.09, ay=0.5,
                            showarrow=True, arrowhead=2, arrowsize=2, arrowwidth=2, arrowcolor="white")

flow_fig.update_layout(
    xaxis=dict(visible=False), yaxis=dict(visible=False),
    template="plotly_dark", height=300, showlegend=False,
    plot_bgcolor='#0d1117', paper_bgcolor='#0d1117',
    margin=dict(l=20, r=20, t=20, b=20)
)

st.plotly_chart(flow_fig, use_container_width=True)

# ETHICAL COMPARISON RADAR
st.subheader("⚖️ Comparative Ethical Impact Radar")

variables = ['Risk', 'Autonomy', 'Reversibility', 'Precision', 'Regeneration']
traditional = [70, 30, 20, 45, 10]  # Higher = worse
neuroguard = [15, 90, 85, 95, 95]   # Higher = better

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
