import dash
from dash import dcc, html
import dash_table
import plotly.graph_objs as go
from dash.dependencies import Input, Output  # Add this line
# Import df from data_collection.py
from data_collection import df, fetch_historical_data


app = dash.Dash(__name__)

# Add a dropdown menu to the Dash app
dropdown = dcc.Dropdown(
    id='dropdown',
    options=[{'label': i, 'value': i} for i in df['id'].unique()],
    value=df['id'].iloc[0]
)

# Update the table based on the selected value


@app.callback(
    Output('table', 'data'),
    Input('dropdown', 'value')
)
def update_table(selected_value):
    filtered_df = df[df['id'] == selected_value]
    return filtered_df.to_dict('records')


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

# Update the line chart based on the selected value


@app.callback(
    Output('line-chart', 'figure'),
    Input('dropdown', 'value')
)
def update_line_chart(selected_value):
    # Fetch historical data for the selected cryptocurrency
    df_historical = fetch_historical_data(selected_value, 30)

    # Create a line chart for price changes over time
    line_chart = go.Scatter(
        x=df_historical['time'],
        y=df_historical['prices'],
        mode='lines',
        name='Price'
    )

    line_chart_layout = go.Layout(
        title='Price Changes Over Time',
        xaxis=dict(
            title='Time'
        ),
        yaxis=dict(
            title='Price'
        ),
    )

    line_chart_fig = go.Figure(data=[line_chart], layout=line_chart_layout)

    return line_chart_fig

# Update the pie chart based on the selected value


@app.callback(
    Output('pie-chart', 'figure'),
    Input('dropdown', 'value')
)
def update_pie_chart(selected_value):
    # Filter the dataframe based on the selected value
    filtered_df = df[df['id'] == selected_value]

    # Create a pie chart of market cap distribution
    pie_chart = go.Pie(
        labels=filtered_df['id'],
        values=filtered_df['market_cap'],
        name='Market Cap'
    )

    pie_chart_layout = go.Layout(
        title='Market Cap Distribution',
    )

    pie_chart_fig = go.Figure(data=[pie_chart], layout=pie_chart_layout)

    return pie_chart_fig


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
    dcc.Graph(
        id='line-chart',
    ),
    dcc.Graph(
        id='pie-chart',
    ),
    html.Div(id='dropdown-container', children=[dropdown]),
    html.Div(id='table-container', children=[table])
])

if __name__ == '__main__':
    app.run_server(debug=True)
