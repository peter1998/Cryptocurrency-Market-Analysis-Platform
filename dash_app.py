# E:\TODO 1337\My Projects\Cryptocurrency-Market-Analysis-Platform\dash_app.py
import dash
from dash import dcc, html
import dash_table
import plotly.graph_objs as go
from data_collection import df  # Import df from data_collection.py

app = dash.Dash(__name__)

# Create a table to display the data
table = dash_table.DataTable(
    id='table',
    columns=[{"name": i, "id": i}
             for i in df.columns if i != 'roi'],  # Exclude 'roi' column
    data=df.to_dict('records'),
)

# Create a histogram for current price
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

# Create a bar chart for market cap
bar_chart = go.Bar(
    x=df['id'],
    y=df['market_cap'],
    name='Market Cap'
)

bar_chart_layout = go.Layout(
    title='Market Cap of Different Cryptocurrencies',
    xaxis=dict(
        title='Cryptocurrency'
    ),
    yaxis=dict(
        title='Market Cap'
    ),
)

bar_chart_fig = go.Figure(data=[bar_chart], layout=bar_chart_layout)

# Create a scatter plot for current price vs total volume
scatter_plot = go.Scatter(
    x=df['current_price'],
    y=df['total_volume'],
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

scatter_plot_layout = go.Layout(
    title='Current Price vs Total Volume',
    xaxis=dict(
        title='Current Price'
    ),
    yaxis=dict(
        title='Total Volume'
    ),
)

scatter_plot_fig = go.Figure(data=[scatter_plot], layout=scatter_plot_layout)

app.layout = html.Div(children=[
    html.H1(children='Cryptocurrency Market Analysis Platform'),
    dcc.Graph(
        id='scatter-plot',
        figure=scatter_plot_fig
    ),
    dcc.Graph(
        id='histogram',
        figure=histogram_fig
    ),
    dcc.Graph(
        id='bar-chart',
        figure=bar_chart_fig
    ),
    html.Div(id='table-container', children=[table])
])

if __name__ == '__main__':
    app.run_server(debug=True)
