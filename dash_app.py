import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
from main import y_test, predictions, df  # Import df from main.py

app = dash.Dash(__name__)

scatter = go.Scatter(
    x=y_test,
    y=predictions,
    mode='markers',
    marker=dict(
        size=10,
        color='rgba(152, 0, 0, .8)',
        line=dict(
            width=2,
            color='rgb(0, 0, 0)'
        )
    )
)

layout = go.Layout(
    title='Actual vs Predicted',
    xaxis=dict(
        title='Actual',
        gridcolor='rgb(255, 255, 255)',
        zerolinewidth=1,
        ticklen=5,
        gridwidth=2,
    ),
    yaxis=dict(
        title='Predicted',
        gridcolor='rgb(255, 255, 255)',
        zerolinewidth=1,
        ticklen=5,
        gridwidth=2,
    ),
)

fig = go.Figure(data=[scatter], layout=layout)

# Create histogram
histogram = go.Histogram(
    x=df['current_price'],
    name='Current Price',
    marker=dict(
        color='rgb(0, 0, 100)'
    )
)

histogram_layout = go.Layout(
    title='Current Price Distribution',
    xaxis=dict(
        title='Current Price'
    ),
    yaxis=dict(
        title='Count'
    ),
    bargap=0.2
)

histogram_fig = go.Figure(data=[histogram], layout=histogram_layout)

app.layout = html.Div(children=[
    html.H1(children='Cryptocurrency Market Analysis Platform'),
    dcc.Graph(
        id='scatter-plot',
        figure=fig
    ),
    dcc.Graph(
        id='histogram',
        figure=histogram_fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
