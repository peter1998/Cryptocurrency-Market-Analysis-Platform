import dash
from dash import dcc, html
import dash_table
import plotly.graph_objs as go
from dash.dependencies import Input, Output
from data_collection import df, fetch_historical_data
import numpy as np
from dash import html

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

time_range_dropdown = dcc.Dropdown(
    id='time-range-dropdown',
    options=[
        {'label': 'Last 7 days', 'value': 7},
        {'label': 'Last 30 days', 'value': 30},
        {'label': 'Last 90 days', 'value': 90},
        {'label': 'Last 1 year', 'value': 365}
    ],
    value=30,  # Default value
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
    title='Current Price Distribution of Top Cryptocurrencies',
    xaxis=dict(
        title='Current Price'
    ),
    yaxis=dict(
        title='Count'
    ),
    bargap=0.2,
    annotations=[
        dict(
            x=0.5,
            y=-0.3,  # Adjust the y position to avoid overlap with xaxis title
            showarrow=False,
            text="This histogram shows the distribution of current prices for the top cryptocurrencies. It helps us understand the common price range for these cryptocurrencies.",
            xref="paper",
            yref="paper",
            font=dict(
                size=15,  # Adjust font size
                color="black"  # Adjust font color
            ),
            align="center",  # Center align the text
            bordercolor='black',  # Add border color
            borderwidth=2,  # Add border width
            borderpad=4,  # Add padding within the border
            bgcolor='white',  # Add background color
            opacity=0.8  # Adjust the opacity
        )
    ],
    autosize=True,  # Enable autosizing to fit the plot within the div
    margin=dict(
        l=50,  # Adjust left margin
        r=50,  # Adjust right margin
        b=100,  # Adjust bottom margin to accommodate the annotation
        t=100,  # Adjust top margin
        pad=10  # Add padding
    )
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
    annotations=[
        dict(
            x=0.5,
            y=-0.3,
            showarrow=False,
            text="This bar chart shows the market capitalization of the top 18 cryptocurrencies. It helps us understand the size of each cryptocurrency in the market.",
            xref="paper",
            yref="paper",
            font=dict(
                size=15,
                color="black"
            ),
            align="center",
            bordercolor='black',
            borderwidth=2,
            borderpad=4,
            bgcolor='white',
            opacity=0.8
        )
    ],
    autosize=True,
    margin=dict(
        l=50,
        r=50,
        b=100,
        t=100,
        pad=10
    )
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
    hovermode='closest',
    annotations=[
        dict(
            x=0.5,
            y=-0.3,
            showarrow=False,
            text="This scatter plot shows the relationship between the current price and total volume of the top 18 cryptocurrencies. It helps us understand how the price and volume are correlated.",
            xref="paper",
            yref="paper",
            font=dict(
                size=13,
                color="black"
            ),
            align="center",
            bordercolor='black',
            borderwidth=2,
            borderpad=4,
            bgcolor='white',
            opacity=0.8
        )
    ],
    autosize=True,
    margin=dict(
        l=50,
        r=50,
        b=100,
        t=100,
        pad=10
    )
)

scatter_plot_fig = go.Figure(data=[scatter_plot], layout=scatter_plot_layout)

# Update the line chart based on the selected value


@app.callback(
    Output('line-chart', 'figure'),
    [Input('dropdown', 'value'),
     Input('time-range-dropdown', 'value')]
)
def update_line_chart(selected_value, selected_time_range):
    # Fetch historical data for the selected cryptocurrency and time range
    df_historical = fetch_historical_data(
        df[df['symbol'] == selected_value]['id'].values[0], selected_time_range)

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
    html.Div(id='table-container', children=[table]),
    html.Div(id='time-range-dropdown-container',
             children=[time_range_dropdown]),
])

if __name__ == '__main__':
    app.run_server(debug=True)
