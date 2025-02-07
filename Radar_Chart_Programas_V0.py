import plotly.graph_objects as go

categories = ['Custos', 'Prazo', 'Qualidade', 'Melhoria contínua']

# Neon pink and lemon green color codes
neon_pink = '#F20FFA'  # Hot Pink
neon_green = '#04DBBB' # Light Green (Lemon-ish)

fig = go.Figure()

fig.add_trace(go.Scatterpolar(
    r=[1, 5, 3, 4],
    theta=categories,
    fill='toself',
    name='Programa A',
    line=dict(color=neon_pink, width=3), # Neon pink line
    fillcolor=neon_green,               # Neon green fill
    opacity=0.7                          # Adjust opacity for neon effect
))

fig.update_layout(
    polar=dict(
        radialaxis=dict(
            visible=True,
            range=[0, 5],
            gridcolor=neon_pink,      # Pink grid lines
            tickcolor=neon_pink,      # Pink tick marks
            linecolor=neon_pink       # Pink radial axis line
        ),
        angularaxis=dict(
            gridcolor=neon_pink,      # Pink angular grid lines
            tickcolor=neon_pink,      # Pink tick marks
            linecolor=neon_pink       # Pink angular axis line
        )
    ),
    showlegend=False,
    paper_bgcolor='rgba(0,0,0,0)',   # Transparent background
    plot_bgcolor='rgba(0,0,0,0)'    # Transparent plot area
)

fig.show()