import plotly.graph_objects as go

def create_figure():
    return go.Figure()
  
def plot_figure(fig, data=[]):  
    x_axis = [int(x) * 50 for x in range(0, len(data)) ]
    y_axis = data
    fig.add_scatter(
        x=x_axis, 
        y=y_axis,
        mode="lines+markers", 
        textposition="bottom center",
        name="AVG Train Cost",
        line={"color": "rgb(0, 0, 200)", "width": 1}
    )
    fig.update_layout(
        title="Cost chart",
        xaxis_title="Number of Iterations",
        yaxis={"title": "Avg Cost", "tickformat": ".5f"},
        font=dict(
            family="Courier New, monospace",
            size=14,
            color="#7f7f7f"
        )
    )
    fig.show()