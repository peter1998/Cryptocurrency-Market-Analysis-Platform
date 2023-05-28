# E:\TODO 1337\My Projects\Cryptocurrency-Market-Analysis-Platform\dash_app.py
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

# Create bar chart for trading volume
bar_chart = go.Bar(
    x=df.index,  # Use the DataFrame index as the x-axis
    y=df['total_volume'],
    name='Trading Volume'
)

bar_chart_layout = go.Layout(
    title='Trading Volume of Different Cryptocurrencies',
    xaxis=dict(
        title='Cryptocurrency'
    ),
    yaxis=dict(
        title='Trading Volume'
    ),
)

bar_chart_fig = go.Figure(data=[bar_chart], layout=bar_chart_layout)

# Create pie chart for market cap
pie_chart = go.Pie(
    labels=df.index,  # Use the DataFrame index as the labels
    values=df['market_cap'],
    name='Market Cap'
)

pie_chart_layout = go.Layout(
    title='Market Cap Distribution Among Different Cryptocurrencies'
)

pie_chart_fig = go.Figure(data=[pie_chart], layout=pie_chart_layout)

app.layout = html.Div(children=[
    html.H1(children='Cryptocurrency Market Analysis Platform'),
    dcc.Graph(
        id='scatter-plot',
        figure=fig
    ),
    dcc.Graph(
        id='histogram',
        figure=histogram_fig
    ),
    dcc.Graph(
        id='bar-chart',
        figure=bar_chart_fig
    ),
    dcc.Graph(
        id='pie-chart',
        figure=pie_chart_fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
