import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
from main import y_test, predictions

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

app.layout = html.Div(children=[
    html.H1(children='Cryptocurrency Market Analysis Platform'),
    dcc.Graph(
        id='scatter-plot',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)