import dash
from dash import dcc, html
import dash_table
import plotly.graph_objs as go
from dash.dependencies import Input, Output
from data_collection import df, fetch_historical_data
import numpy as np

app = dash.Dash(__name__)

# Filter the dataframe to include only the top 18 cryptocurrencies
top_cryptos = ['bitcoin', 'ethereum', 'tether', 'binancecoin', 'usd-coin', 'xrp', 'cardano', 'dogecoin', 'polygon',
               'solana', 'tron', 'litecoin', 'polkadot', 'binance-usd', 'shiba-inu', 'avalanche-2', 'dai', 'wrapped-bitcoin']
df = df[df['id'].isin(top_cryptos)]

# Add a dropdown menu to the Dash app
dropdown = dcc.Dropdown(
    id='dropdown',
    options=[{'label': html.Div([html.Img(src=i['image'], style={'height': '20px', 'width': '20px'}),
                                i['symbol']]), 'value': i['symbol']} for i in df.to_dict('records')],
    value=df['symbol'].iloc[0],
    style={
        'backgroundColor': '#d6d6d6',
        'color': '#000000'
    }
)


@app.callback(
    Output('table', 'data'),
    Input('dropdown', 'value')
)
def update_table(selected_value):
    filtered_df = df[df['symbol'] == selected_value]
    return filtered_df.to_dict('records')


table = dash_table.DataTable(
    id='table',
    columns=[{"name": i, "id": i} for i in df.columns if i != 'roi'],
    data=df.to_dict('records'),
    style_data_conditional=[
        {
            'if': {'row_index': 'odd'},
            'backgroundColor': 'rgb(248, 248, 248)'
        },
        {
            'if': {'row_index': 'even'},
            'backgroundColor': 'rgb(255, 255, 255)'
        },
        {
            'if': {'state': 'active'},  # 'active' | 'selected'
            'backgroundColor': 'rgb(210, 210, 210)',
            'border': '1px solid rgb(0, 116, 217)'
        },
    ],
    style_header={
        'backgroundColor': 'rgb(230, 230, 230)',
        'fontWeight': 'bold'
    },
)


histogram = go.Histogram(
    x=df['current_price'],
    name='Current Price',
    marker=dict(
        color='rgb(0, 0, 100)'
    ),
    hoverinfo='x+y',  # Show the exact number of cryptocurrencies in each price bin
    hoverlabel=dict(  # Customize the hover label
        bgcolor='white',  # Background color
        font_size=16,  # Font size
        font_family='Rockwell'  # Font family
    )
)

histogram_layout = go.Layout(
    title='Current Price Distribution of Top 18 Cryptocurrencies',  # Add a title
    xaxis=dict(
        title='Current Price (USD)'  # Label the x axis
    ),
    yaxis=dict(
        title='Number of Cryptocurrencies'  # Label the y axis
    ),
    bargap=0.2
)

histogram_fig = go.Figure(data=[histogram], layout=histogram_layout)


bar_chart = go.Bar(
    x=df['id'],
    y=np.log(df['market_cap']),  # Use log scale for large values
    name='Market Cap',
    text=df['id'],  # Add cryptocurrency names as hover text
    hoverinfo='text+y'  # Show hover info
)

bar_chart_layout = go.Layout(
    title='Market Cap of Top 18 Cryptocurrencies',
    xaxis=dict(
        title='Cryptocurrency'
    ),
    yaxis=dict(
        title='Market Cap (log scale)'
    ),
)

bar_chart_fig = go.Figure(data=[bar_chart], layout=bar_chart_layout)

scatter_plot = go.Scatter(
    x=df['current_price'],
    y=np.log(df['total_volume']),  # Use log scale for large values
    mode='markers',
    marker=dict(
        size=10,
        # Use different colors for different cryptocurrencies
        color=df['id'].astype('category').cat.codes,
        colorscale='Rainbow',  # Choose a colorscale
        line=dict(
            width=2,
            color='rgb(0, 0, 0)'
        )
    ),
    text=df['id'],  # Add cryptocurrency names as hover text
    hoverinfo='text+x+y'  # Show hover info
)

scatter_plot_layout = go.Layout(
    title='Current Price vs Total Volume for Top 18 Cryptocurrencies',
    xaxis=dict(
        title='Current Price'
    ),
    yaxis=dict(
        title='Total Volume (log scale)'
    ),
    hovermode='closest'
)

scatter_plot_fig = go.Figure(data=[scatter_plot], layout=scatter_plot_layout)

# Update the line chart based on the selected value


@app.callback(
    Output('line-chart', 'figure'),
    Input('dropdown', 'value')
)
def update_line_chart(selected_value):
    # Fetch historical data for the selected cryptocurrency
    df_historical = fetch_historical_data(
        df[df['symbol'] == selected_value]['id'].values[0], 30)

    # Create a line chart for price changes over time
    line_chart = go.Scatter(
        x=df_historical['time'],
        y=df_historical['price'],
        mode='lines',
        name='Price'
    )

    line_chart_layout = go.Layout(
        title=f'Price Changes Over Time for {selected_value.capitalize()}',
        xaxis=dict(
            title='Time'
        ),
        yaxis=dict(
            title='Price'
        ),
    )

    line_chart_fig = go.Figure(data=[line_chart], layout=line_chart_layout)

    return line_chart_fig


@app.callback(
    Output('pie-chart', 'figure'),
    Input('dropdown', 'value')
)
def update_pie_chart(selected_value):
    # Ignore the selected value and use the entire dataframe
    # filtered_df = df[df['symbol'] == selected_value]

    # Create a pie chart of market cap distribution
    pie_chart = go.Pie(
        labels=df['id'],
        values=df['market_cap'],
        name='Market Cap'
    )

    pie_chart_layout = go.Layout(
        title='Market Cap Distribution for Top 18 Cryptocurrencies',
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
