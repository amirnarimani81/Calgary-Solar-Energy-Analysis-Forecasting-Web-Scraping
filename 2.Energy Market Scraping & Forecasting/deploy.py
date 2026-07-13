# =========================================
# Energy Sector Dashboard - Full Streamlit App
# =========================================

import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.graph_objects as go
from prophet import Prophet
from sklearn.metrics import mean_squared_error
import math
import requests
from bs4 import BeautifulSoup

# -------------------------
# 1️ Scrape Revenue Function
# -------------------------
header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}

def scrape_revenue(url):
    html = requests.get(url, headers=header).text
    soup = BeautifulSoup(html, "html.parser")
    tables = soup.find_all("table")
    if not tables:
        return pd.DataFrame(columns=["Date","Revenue"])
    table = tables[0]   
    rows = table.find_all("tr")
    df = pd.DataFrame(columns=["Date", "Revenue"])
    for row in rows[1:]:
        cols = row.find_all("td")
        if len(cols) >= 2:
            date = cols[0].text.strip()
            revenue = cols[1].text.strip().replace(",", "").replace("$","")
            if revenue:
                df.loc[len(df)] = [date, revenue]
    df["Revenue"] = df["Revenue"].astype(float)
    return df

# -------------------------
# 2️ Companies & URLs
# -------------------------
companies = {
    "Chevron": "CVX",
    "Total Energies": "TTE",
    "Canadian Natural Resources": "CNQ",
    "Suncor Energy": "SU",
    "Shell": "SHEL",
    "Exxon Mobil": "XOM"}

revenue_urls = {
    "Chevron": "https://www.macrotrends.net/stocks/charts/CVX/chevron/revenue",
    "Total Energies": "https://www.macrotrends.net/stocks/charts/TTE/total-energies/revenue",
    "Canadian Natural Resources": "https://www.macrotrends.net/stocks/charts/CNQ/canadian-natural-resources/revenue",
    "Suncor Energy": "https://www.macrotrends.net/stocks/charts/SU/suncor-energy/revenue",
    "Shell": "https://www.macrotrends.net/stocks/charts/SHEL/shell/revenue",
    "Exxon Mobil": "https://www.macrotrends.net/stocks/charts/XOM/exxon-mobil/revenue"}

# -------------------------
# 3️ Prophet Forecast Function
# -------------------------
def prophet_forecast(df, periods=90):
    """
    df: DataFrame with columns ['Date', 'Close']
    periods: Number of days to forecast
    Returns: model, forecast, RMSE
    """
    # Ensure datetime is proper and remove timezone
    df['Date'] = pd.to_datetime(df['Date'])
    df_prophet = df[['Date','Close']].rename(columns={'Date':'ds','Close':'y'})
    df_prophet['ds'] = df_prophet['ds'].dt.tz_localize(None)  # remove timezone

    # Fit Prophet model
    model = Prophet(daily_seasonality=False, weekly_seasonality=True, yearly_seasonality=True)
    model.fit(df_prophet)

    # Forecast
    future = model.make_future_dataframe(periods=periods)
    forecast = model.predict(future)

    # Compute RMSE on historical
    merged = forecast[['ds','yhat']].merge(df_prophet, on='ds', how='left')
    hist = merged[merged['y'].notna()]
    rmse = math.sqrt(mean_squared_error(hist['y'], hist['yhat']))

    return model, forecast, rmse


# -------------------------
# 4 Multi-Company Comparison
# -------------------------
def compare_companies_closes(companies):
    fig = go.Figure()
    for name, ticker in companies.items():
        df = yf.Ticker(ticker).history(period="5y").reset_index()
        fig.add_trace(go.Scatter(x=df['Date'], y=df['Close'], mode='lines', name=name))
    fig.update_layout(title="Stock Price Comparison (Last 5 Years)", xaxis_title="Date", yaxis_title="Close Price ($)", template="plotly_white")
    return fig

# -------------------------
# 5️ Price Jump Alerts
# -------------------------
def check_price_alerts(df, threshold=5):
    df_alert = df.copy()
    df_alert['Change %'] = df_alert['Close'].pct_change()*100
    alerts = df_alert[(df_alert['Change %'].abs() >= threshold)]
    return alerts[['Date','Close','Change %']]

# -------------------------
# Utility: Annual % Change
# -------------------------
def annual_percent_change(df):
    """Calculate YoY % change based on year-end close."""
    if df.empty or "Date" not in df.columns or "Close" not in df.columns:
        return pd.DataFrame()

    df['Year'] = pd.to_datetime(df['Date']).dt.year
    df_year = df.groupby("Year")['Close'].last().reset_index()
    df_year['Annual % Change'] = df_year['Close'].pct_change() * 100
    return df_year


# -------------------------
# Sidebar Navigation
# -------------------------
st.sidebar.title('Navigation')
page = st.sidebar.radio("Go to:", [
    "Home",
    "Energy Sector Analytics",
    "Prophet Forecast"])


# =========================================
#  HOME PAGE
# =========================================
if page == "Home":
    st.title("Energy Sector Stock & Revenue Forecasting System")

    try:
        st.image(
            r"D:\Data Analysis- Scientist\Projects\Web Scrapping-Energy sector stocks\how-to-scrape-yahoo-finance.jpg",
            use_container_width=True
        )
    except:
        st.info("Cover image not found—skipping.")

    st.markdown("""
### Project Objective
Create a full automated analytics system for tracking and forecasting financial performance of global energy companies
 (Chevron, TotalEnergies, Canadian Natural Resource , Suncor, Exxon Mobil, Shell) .

### What this system includes:
- Real-time stock data (Yahoo Finance)
- Revenue scraping (Macrotrends)
- Clean ETL pipeline
- Machine-learning forecasting (Prophet)
- Interactive dashboards (Plotly)
- Alerts (price jumps)
- Multi-company comparisons
""")

    st.markdown("---")
    st.subheader("Why This Project Is Important")

    tab1, tab2, tab3 = st.tabs([
        "Energy Forecasting",
        "Prophet Model",
        "RMSE"])

    with tab1:
        st.write("Energy markets are volatile, driven by geopolitics and global demand cycles.")

    with tab2:
        st.write("Prophet handles seasonal behavior and trend changes with minimal tuning.")

    with tab3:
        st.write("RMSE measures accuracy of historical fit.")


# =========================================
#  ENERGY SECTOR ANALYTICS PAGE
# =========================================
elif page == "Energy Sector Analytics":

    st.header("Energy Sector Analytics")

    choice = st.sidebar.selectbox("Select a Company", list(companies.keys()))
    ticker = companies[choice]

    # Load stock data
    try:
        stock_df = yf.Ticker(ticker).history(period="max").reset_index()
    except:
        stock_df = pd.DataFrame()

    # Revenue scrape
    revenue_df = scrape_revenue(revenue_urls.get(choice, ""))

    # ========== KPIs ==========
    colA, colB, colC = st.columns(3)
    colA.metric("Selected Company", choice)

    if not stock_df.empty:
        colB.metric("Latest Stock Price", f"${stock_df['Close'].iloc[-1]:.2f}")
    else:
        colB.metric("Latest Stock Price", "N/A")

    colC.metric("Forecast Horizon", "90 Days")


    # ========== Stock + Revenue ==========
    st.subheader("Stock Price & Revenue Overview")
    c1, c2 = st.columns([2,1])

    with c1:
        st.write(" Stock Price (Head)")
        st.dataframe(stock_df.head())

    with c2:
        st.write(" Revenue Table (Head)")
        st.dataframe(revenue_df.head())

    # Combined chart
    fig = go.Figure()

    if not stock_df.empty:
        fig.add_trace(go.Scatter(x=stock_df['Date'], y=stock_df['Close'],
                                 mode='lines', name='Stock Price'))

    if not revenue_df.empty:
        revenue_df['Date'] = pd.to_datetime(revenue_df['Date'])
        fig.add_trace(go.Bar(x=revenue_df['Date'], y=revenue_df['Revenue'],
                             name='Revenue', opacity=0.45, yaxis='y2'))

    fig.update_layout(title=f"{choice}: Stock vs Revenue",
                      template="plotly_white")
    st.plotly_chart(fig, use_container_width=True)

    st.markdown("---")

    # Multi-company comparison
    st.subheader("Multi-Company Price Comparison (5 years)")
    st.plotly_chart(compare_companies_closes(companies), use_container_width=True)

    st.markdown("---")

    # Alerts
    st.subheader("Price Jump Alerts (±5%)")
    alerts = check_price_alerts(stock_df)
    if alerts.empty:
        st.success("No major price jumps detected.")
    else:
        st.error("Significant price jumps detected:")
        st.dataframe(alerts)

    st.markdown("---")

    # Annual % change
    st.subheader("Annual % Change (YoY)")
    df_yearly = annual_percent_change(stock_df)

    if not df_yearly.empty:
        colors = ['green' if x >= 0 else 'red' for x in df_yearly['Annual % Change']]
        fig2 = go.Figure()
        fig2.add_trace(go.Bar(
            x=df_yearly['Year'].astype(str),
            y=df_yearly['Annual % Change'],
            marker_color=colors,
            text=df_yearly['Annual % Change'].map(lambda x: f"{x:.2f}%"),
            textposition='auto'))
        fig2.update_layout(
            title=f"{choice} Annual % Change",
            xaxis_title="Year",
            yaxis_title="YoY Change (%)",
            template="plotly_white" )
        st.plotly_chart(fig2, use_container_width=True)


# =========================================
#  PROPHET FORECAST PAGE
# =========================================

# =========================================
#  PROPHET FORECAST PAGE
# =========================================

elif page == "Prophet Forecast":

    st.header("🔮 Prophet Forecast – 90 Day Outlook")

    choice = st.sidebar.selectbox(
        "Select Company for Forecast",
        list(companies.keys()))

    ticker = companies[choice]

    # =========================
    # Download Stock Data
    # =========================
    try:

        stock_df = yf.Ticker(ticker).history(
            period="max")

        # Reset index
        stock_df = stock_df.reset_index()

        # Keep required columns
        stock_df = stock_df[["Date", "Close"]]

        # Convert date
        stock_df["Date"] = pd.to_datetime(
            stock_df["Date"])

        # Remove timezone
        try:
            stock_df["Date"] = (
                stock_df["Date"]
                .dt.tz_localize(None))
        except:
            pass

        # Convert Close
        stock_df["Close"] = pd.to_numeric(
            stock_df["Close"],
            errors="coerce")

        # Clean data
        stock_df = stock_df.dropna()

        # Remove duplicate dates - KEEP THE MOST RECENT VALUE FOR EACH DATE
        stock_df = stock_df.groupby("Date", as_index=False).last()

        # Sort data
        stock_df = (
            stock_df
            .sort_values("Date")
            .reset_index(drop=True))


    except Exception as e:

        st.error("Unable to download stock data")
        st.exception(e)
        st.stop()


    # =========================
    # Check Data Size
    # =========================

    if len(stock_df) < 100:

        st.warning(
            "Not enough historical data for forecasting.")
        st.stop()


    # =========================
    # Prophet Preparation
    # =========================
    prophet_df = ( stock_df.rename(columns={
                "Date": "ds",
                "Close": "y" }).drop_duplicates(subset="ds",keep="last" ))

    # =========================
    # Train Prophet
    # =========================
    model = Prophet(
        yearly_seasonality=True,
        weekly_seasonality=True,
        daily_seasonality=False)

    model.fit(prophet_df)

    # =========================
    # Forecast
    # =========================
    future = model.make_future_dataframe(
        periods=90)

    forecast = model.predict( future)
    # =========================
    # RMSE
    # =========================
    history = forecast[
        ["ds", "yhat"]].merge( prophet_df,on="ds",how="inner")
    rmse = math.sqrt( mean_squared_error( history["y"],history["yhat"]))


    st.metric("RMSE (Historical Fit)",f"{rmse:.2f}")
    # =========================
    # Forecast Plot
    # =========================
    fig = go.Figure()
    fig.add_trace(
        go.Scatter(
            x=stock_df["Date"],
            y=stock_df["Close"],
            mode="lines",
            name="Historical Price"))

    fig.add_trace(
        go.Scatter(
            x=forecast["ds"],
            y=forecast["yhat"],
            mode="lines",
            name="Forecast"))


    fig.update_layout(
        title=f"{choice} Stock Price Forecast - 90 Days",
        xaxis_title="Date",
        yaxis_title="Price ($)",
        template="plotly_white")

    st.plotly_chart(fig, use_container_width=True)


    # =========================
    # Prophet Components
    # =========================
    if st.checkbox("Show Forecast Components"): component_fig = model.plot_components(forecast)
    st.pyplot( component_fig)