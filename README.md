# Cryptocurrency Market Analysis Platform

## Description
This platform uses data science techniques and Dash, a Python framework for building analytical web applications, to analyze cryptocurrency market trends. It includes modules for data collection, processing, visualization, and an interactive user interface. It also applies machine learning models to make predictions.

![image](https://github.com/peter1998/Cryptocurrency-Market-Analysis-Platform/assets/19347046/39590517-a55e-4910-8444-7f4d26a9759d)
![image](https://github.com/peter1998/Cryptocurrency-Market-Analysis-Platform/assets/19347046/f1b1b09e-dc0a-4a07-bdc8-9ece0a8f40f9)

## Modules

### Data Collection
This module uses APIs to fetch real-time data for various cryptocurrencies, focusing on the top 18 cryptocurrencies by market cap.

### Data Processing
This module cleans and transforms the raw data into a format suitable for visualization and user interaction. It processes the fetched data by converting numerical columns to numeric type, handling missing values, detecting and removing outliers, and creating new features.

### Machine Learning
The machine learning module trains different regression models on the processed data and makes predictions. The models used are Linear Regression, Decision Tree Regressor, K-Nearest Neighbors Regressor, and Support Vector Regressor.

### Model Comparison
The performance of the models is compared using cross-validation and the mean squared error (MSE) as the performance metric. The results are printed and also visualized using a boxplot.

![image](https://github.com/peter1998/Cryptocurrency-Market-Analysis-Platform/assets/19347046/31902a61-8b00-4cbb-90e0-208cfffed4fa)


The above plot is a boxplot comparison of the performance of different regression models on the dataset. Each box represents the distribution of cross-validation scores for a model. The line in the middle of the box is the median score, the box itself spans from the first quartile (25th percentile) to the third quartile (75th percentile), and the whiskers extend to show the range of the scores. Outliers may be plotted as individual points. The models being compared are Linear Regression (LR), Decision Tree Regressor (DTR), K-Nearest Neighbors Regressor (KNR), and Support Vector Regressor (SVR).

### Visualization
This module uses Plotly, a Python graphing library, to create interactive, publication-quality graphs. It includes histograms, bar charts, scatter plots, and line charts to display current price distribution, market cap, price vs volume, and price changes over time.

### User Interface
This module uses Dash to create an interactive web-based user interface. Users can select a specific cryptocurrency from a dropdown menu to view detailed information and charts.

## Technologies Used
- Python
- Data Processing Libraries (pandas)
- Data Visualization Libraries (Plotly)
- Web Framework (Dash)

## Setup and Installation
To start up the main application, navigate to the project directory in your terminal and run the following command:
- python main.py

To start up the Dash app, navigate to the project directory in your terminal and run the following command:
- python dash_app.py

## Usage
To use this project, follow these steps:

Clone the repository to your local machine.
Install the required Python packages using pip: pip install -r requirements.txt
Run the main application: python main.py
Run the Dash app: python dash_app.py
Open a web browser and navigate to localhost:8050 to view the app.

## Contributing
open an issue and come build data science projects with me

## License
No Information about the project's license

## Future Work
There are several ways this platform could be further improved:

Adding More Data Sources: Incorporating more data sources could provide a more comprehensive view of the cryptocurrency market. This could include social media sentiment, news articles, or other financial indicators.

Advanced Analysis Techniques: Implementing more advanced analysis techniques, such as machine learning or time series forecasting, could improve the accuracy of the market trend predictions.

User Interface Improvements: The user interface could be made more intuitive and user-friendly. This could include better navigation, more detailed explanations of the data, or customizable charts.

Real-Time Updates: Implementing real-time updates would allow the platform to provide up-to-the-minute market information.

Alerts and Notifications: Users could receive alerts or notifications when significant market events occur, such as drastic price changes or unusual trading volume.

Enhanced Machine Learning Models: The machine learning module could be expanded to include more models or to optimize the hyperparameters of the existing models. This could improve the accuracy of the predictions.

Integration with Other Financial Data: The platform could be expanded to include data from other financial markets, such as stocks or commodities. This could provide a more comprehensive view of the financial landscape.

Expanded Visualization Capabilities: The visualization module could be expanded to include more types of charts or to provide more customization options. This could allow users to explore the data in more depth.

Expanded User Interface Features: The user interface could be expanded to include more features, such as the ability to save or share charts, or to set up custom alerts or notifications.
