<h1 align="center">
Energy Analytics Intelligence Platform
</h1>

<p align="center">
<strong>
From Renewable Energy Data and Financial Markets to Predictive Business Intelligence
</strong>
</p>

<p align="center">
A Full-Stack Data Analytics Platform Combining Energy Data Engineering, Machine Learning Forecasting, Web Scraping, and Interactive Business Intelligence
</p>

<hr>


<h2> Project Overview</h2>

<p>
Energy systems are becoming increasingly data-driven. Renewable energy integration, market volatility, and increasing operational complexity require organizations to move beyond traditional reporting approaches and adopt intelligent analytics platforms capable of transforming raw data into actionable decisions.
</p>


<p>
This project presents an end-to-end <strong>Energy Analytics Intelligence Platform</strong> designed to solve real-world challenges across two important areas of the energy sector:
</p>


<ul>

<li>
<strong>Renewable Energy Intelligence:</strong>
Analyzing and forecasting solar photovoltaic (PV) generation behavior using historical energy production data from Calgary.
</li>


<li>
<strong>Energy Financial Intelligence:</strong>
Monitoring, comparing, and forecasting the financial performance of global energy companies using automated market data collection and machine learning.
</li>

</ul>


<p>
The platform demonstrates the complete lifecycle of a modern energy analytics solution:
</p>


<p align="center">

<strong>
Raw Data → Data Engineering → SQL Analytics → Feature Engineering → Machine Learning → Visualization → Decision Support
</strong>

</p>


<p>
Instead of treating data analysis as a single reporting task, this project focuses on building a scalable analytics workflow that reflects how real organizations use data to improve operational efficiency, reduce uncertainty, and support strategic decisions.
</p>


<hr>


<h2> Why This Project?</h2>


<p>
The energy sector faces complex analytical challenges. Renewable generation is affected by weather conditions, seasonal changes, and operational limitations, while energy companies operate in highly dynamic financial markets influenced by commodity prices, economic conditions, and global demand.
</p>


<p>
Traditional spreadsheet-based approaches often create several limitations:
</p>


<ul>

<li>
Data is collected manually from multiple disconnected sources.
</li>

<li>
Large historical datasets are difficult to analyze efficiently.
</li>

<li>
Decision-makers lack predictive insights about future trends.
</li>

<li>
Operational teams require faster and more reliable information.
</li>

</ul>


<p>
This project addresses these challenges by developing automated analytics pipelines that combine data engineering, statistical analysis, machine learning, and business intelligence into a unified platform.
</p>


<hr>


<h2> Business Problems Addressed</h2>


<h3>1. Renewable Energy Forecasting Challenge</h3>

<img src="Plot/correlation_heatmap.png" width="300">
<p>
Solar energy generation is highly variable because production depends on sunlight availability, seasonal patterns, weather conditions, and installation characteristics.
</p>


<p>
Energy planners need answers to critical questions:
</p>


<ul>

<li>
How much solar energy will be produced in the future?
</li>

<li>
When are peak production periods occurring?
</li>

<li>
Which installations are performing efficiently?
</li>

<li>
How can storage and grid operations be optimized?
</li>

</ul>


<p>
To address this challenge, the project develops a solar PV analytics and forecasting pipeline using Calgary's historical renewable energy data.
</p>



<h3>2. Energy Market Intelligence Challenge</h3>

<h2>🎥 Project Demo Video</h2>

<p align="center">
<video width="800" controls>
<source src="https://github.com/amirnarimani81/Calgary-Solar-Energy-Analysis-Forecasting-Web-Scraping/raw/main/2.Energy%20Market%20Scraping%20%26%20Forecasting/Assest/streamlit-deploy-2026-07-12-23-07-27.webm" type="video/webm">
</video>
</p>

<p>
Energy companies operate in rapidly changing financial environments where stock performance and revenue trends provide important signals for investors and business analysts.
</p>


<p>
However, financial information is distributed across multiple platforms, requiring automated solutions to collect, process, and analyze market data.
</p>


<p>
The financial analytics component addresses questions such as:
</p>


<ul>

<li>
How are major energy companies performing over time?
</li>

<li>
How do revenue trends compare with stock performance?
</li>

<li>
Can machine learning identify future market trends?
</li>

<li>
How can analysts monitor financial changes automatically?
</li>

</ul>


<hr>


<h2> Platform Architecture</h2>


<p>
The platform follows a modular architecture designed around the complete analytics workflow.
</p>


<h3>
1. Data Collection & Ingestion Layer
</h3>


<p>
The first stage focuses on collecting reliable data from different energy-related sources.
</p>


<p>
For renewable energy analytics, historical solar PV generation data is collected from the City of Calgary Open Data Portal.
</p>


<p>
For financial analytics, market information is collected automatically using APIs and web scraping techniques.
</p>


<p>
The data sources include:
</p>


<ul>

<li>
City of Calgary Solar Energy Production Sites Dataset
</li>

<li>
Yahoo Finance market data through yfinance
</li>

<li>
Financial revenue information collected through web scraping using BeautifulSoup and Requests
</li>

</ul>



<h3>
2. Data Engineering & ETL Layer
</h3>


<p>
Raw data rarely arrives in a form suitable for analysis. Therefore, automated ETL pipelines were developed to transform raw information into structured analytical datasets.
</p>


<p>
The ETL workflow includes:
</p>


<ul>

<li>
Data extraction from multiple sources.
</li>

<li>
Data cleaning and quality validation.
</li>

<li>
Missing value and duplicate handling.
</li>

<li>
Feature engineering and transformation.
</li>

<li>
Database storage using SQL-based workflows.
</li>

</ul>


<p>
Python, Pandas, SQLAlchemy, and relational databases were used to create reproducible and scalable data workflows.
</p>


<hr>


<h2> Renewable Energy Analytics Module</h2>


<p>
The renewable energy module focuses on transforming Calgary solar PV generation records into operational intelligence.
</p>


<p>
The dataset contains approximately <strong>258,000 hourly observations</strong> collected from multiple solar installations between <strong>2015 and 2024</strong>.
</p>


<p>
The analysis explores:
</p>


<ul>

<li>
Hourly and seasonal solar generation patterns.
</li>

<li>
Site-level performance differences.
</li>

<li>
Production volatility and operational risks.
</li>

<li>
Future energy generation forecasting.
</li>

</ul>


<p>
The objective is not only to predict energy production but also to provide insights that support:
</p>


<ul>

<li>
Grid integration planning.
</li>

<li>
Energy storage optimization.
</li>

<li>
Maintenance scheduling.
</li>

<li>
Renewable energy strategy development.
</li>

</ul>


<hr>


<h2> Energy Financial Intelligence Module</h2>


<p>
The financial analytics module extends the platform from operational energy data into market intelligence.
</p>


<p>
The system automatically collects and analyzes financial information from major global energy companies to understand relationships between stock performance, revenue trends, and future market behavior.
</p>


<p>
The workflow includes:
</p>


<ul>

<li>
Automated stock price collection using Yahoo Finance.
</li>

<li>
Revenue extraction through web scraping.
</li>

<li>
Financial trend analysis.
</li>

<li>
Stock forecasting using Prophet.
</li>

<li>
Interactive comparison dashboards.
</li>

</ul>


<p>
This demonstrates how data analytics can support both engineering decisions and financial decision-making within the energy industry.
</p>


<hr>
