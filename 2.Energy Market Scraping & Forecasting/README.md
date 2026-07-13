<h1 align="center">
Energy Sector Stock & Revenue Forecasting Dashboard
</h1>

<p align="center">
An End-to-End Energy Financial Intelligence Platform Combining Web Scraping, ETL Pipelines, Machine Learning Forecasting, and Interactive Business Analytics.
</p>


<hr>


<h2>🎥 Demo Video</h2>

<p>
<strong>Video Link:</strong><br>
<!-- Add YouTube / Demo link here -->
</p>


<hr>


<h2> Overview</h2>

<p>
Energy companies operate in highly dynamic markets where stock performance, revenue growth, commodity prices, and global economic conditions continuously influence business decisions.
</p>

<p>
This project develops a full-stack analytics platform to monitor, compare, and forecast the financial performance of major global energy companies (Chevron, Shell, Suncor energy etc). The system transforms raw financial data into meaningful business insights by integrating automated data collection, web scraping, data processing, machine learning forecasting, and interactive visualization.
</p>

<p>
The dashboard combines live stock market information from <strong>Yahoo Finance</strong>, revenue data extracted through <strong>web scraping using BeautifulSoup</strong>, time-series forecasting using <strong>Facebook Prophet</strong>, and interactive analytics developed with <strong>Streamlit and Plotly</strong>.
</p>

<p>
The project demonstrates the complete analytics lifecycle:

<strong>
Data Collection → ETL Processing → Exploratory Analysis → Machine Learning → Visualization → Decision Support
</strong>
</p>


<hr>


<h2>Aim of the Project</h2>

<p>
The main goal of this project is to demonstrate how data analytics and machine learning can be applied to real-world financial and energy-sector problems.
</p>

<p>
The platform was designed to achieve the following objectives:
</p>

<ul>

<li>
Automate the collection and preprocessing of financial market data.
</li>

<li>
Extract company revenue information from online financial sources.
</li>

<li>
Analyze historical stock performance and revenue trends.
</li>

<li>
Develop forecasting models to estimate future stock behavior.
</li>

<li>
Provide interactive dashboards that support financial analysis and decision-making.
</li>

<li>
Create a scalable portfolio-ready analytics application.
</li>

</ul>


<hr>


<h2> Solution Architecture</h2>

<p>
The system follows a modular architecture that connects data engineering, machine learning, and business intelligence components.
</p>


<h3>1. Data Ingestion & Web Scraping</h3>

<p>
The first layer collects financial information automatically from multiple sources.
</p>

<ul>

<li>
Real-time stock prices are retrieved using <strong>Yahoo Finance API (yfinance)</strong>.
</li>

<li>
Quarterly company revenue data is extracted from financial websites using <strong>BeautifulSoup and Requests</strong>.
</li>

<li>
The collected information is transformed into structured datasets for further analysis.
</li>

</ul>


<h3>2. Data Processing & ETL Pipeline</h3>

<p>
The collected financial data is cleaned and prepared through an automated preprocessing workflow.
</p>

<p>
The pipeline performs data validation, datetime conversion, missing value handling, duplicate removal, and feature preparation for financial analysis.
</p>

<p>
Additional financial indicators are generated, including annual percentage changes, historical trends, and stock price movement alerts.
</p>


<h3>3. Machine Learning Forecasting</h3>

<p>
To understand future market behavior, the platform applies Facebook Prophet, a time-series forecasting model designed to capture trends and seasonal patterns.
</p>

<p>
The model generates a 90-day stock price forecast and evaluates historical prediction performance using RMSE (Root Mean Square Error).
</p>

<p>
The forecasting component helps demonstrate how machine learning can support financial planning and market trend analysis.
</p>


<h3>4. Interactive Analytics Dashboard</h3>

<p>
The final layer transforms analytical results into an interactive business intelligence application.
</p>

<p>
Using Streamlit and Plotly, users can explore company performance, compare multiple energy companies, analyze revenue trends, monitor price movements, and visualize forecasting results.
</p>


<hr>


<h2> Key Features</h2>

<ul>

<li>
Live energy company stock monitoring and historical performance analysis.
</li>

<li>
Automated revenue extraction and financial data processing.
</li>

<li>
Machine learning forecasting using Prophet with trend and seasonality analysis.
</li>

<li>
Interactive Plotly charts for financial exploration.
</li>

<li>
Multi-company comparison across major global energy companies.
</li>

<li>
Automatic detection of significant stock price movements.
</li>

<li>
Year-over-Year financial performance analysis.
</li>

</ul>


<hr>


<h2>Business Value & Benefits</h2>

<p>
This platform demonstrates how automated analytics systems can improve financial monitoring and decision support.
</p>

<p>
By combining stock prices, revenue information, and forecasting models into one environment, the dashboard provides a unified view of company performance instead of relying on disconnected spreadsheets and manual analysis.
</p>

<p>
The modular design allows future expansion with additional companies, commodity prices, financial indicators, advanced forecasting models, and automated reporting systems.
</p>


<hr>


<h2> Technology Stack</h2>

<ul>

<li>
<strong>Programming:</strong> Python
</li>

<li>
<strong>Data Collection:</strong> yfinance, Requests, BeautifulSoup
</li>

<li>
<strong>Data Processing:</strong> Pandas, NumPy
</li>

<li>
<strong>Machine Learning:</strong> Facebook Prophet, Scikit-learn
</li>

<li>
<strong>Visualization:</strong> Plotly
</li>

<li>
<strong>Dashboard Development:</strong> Streamlit
</li>

<li>
<strong>Development Tools:</strong> Jupyter Notebook, Git
</li>

</ul>


<hr>


<h2> How to Run</h2>


<h3>Clone Repository</h3>

<pre><code>
git clone https://github.com/yourusername/energy-dashboard.git

cd energy-dashboard
</code></pre>


<h3>Install Dependencies</h3>

<pre><code>
pip install -r requirements.txt
</code></pre>


<h3>Launch Dashboard</h3>

<pre><code>
streamlit run app.py
</code></pre>


<hr>


<h2> Dashboard Pages</h2>


<h3>Home</h3>

<p>
Provides project overview, objectives, architecture explanation, and system introduction.
</p>


<h3>Energy Sector Analytics</h3>

<p>
Allows users to explore stock performance, revenue trends, company comparisons, annual growth analysis, and price movement alerts.
</p>


<h3> Prophet Forecast</h3>

<p>
Provides a 90-day stock price forecast with historical comparison, forecasting results, and trend/seasonality components.
</p>

<img src="assets/correlation_heatmap.png" width="300">
<hr>


<h2> Project Structure</h2>


<pre><code>

energy-dashboard/

│

├── app.py                  # Main Streamlit application

├── requirements.txt        # Python dependencies

├── README.md               # Project documentation

└── assets/                 # Images and project resources

</code></pre>


<hr>


<h2> Project Showcase</h2>

<p>
This project demonstrates practical experience in building an end-to-end analytics product:
</p>

<ul>

<li>
Financial data collection and automated web scraping.
</li>

<li>
ETL pipeline development and data preprocessing.
</li>

<li>
Time-series forecasting using machine learning.
</li>

<li>
Interactive dashboard design and business intelligence reporting.
</li>

<li>
Energy-sector data analytics and decision-support systems.
</li>

</ul>


<hr>


<p align="center">
<strong>
Chemical Engineer | Data Analyst | Energy Sector Analytics | Python | Machine Learning | Business Intelligence
</strong>
</p>