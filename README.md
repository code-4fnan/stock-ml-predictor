# 📈 Stock Market ML Predictor

A stateless web application that predicts the next-day closing price of the Top 10 companies by market capitalization using Machine Learning.

## Features
* **Live Data Ingestion:** Automatically downloads the last 3 years of daily historical closing prices using `yfinance`.
* **On-the-Fly Machine Learning:** Trains a fresh Linear Regression model via `scikit-learn` for each company upon page load.
* **Dynamic Visualization:** Uses `Chart.js` to render a comparative bar graph of current vs. predicted prices.
* **Stateless Architecture:** No database required; data is processed in memory for rapid deployment and testing.

## Tech Stack
* **Backend:** Python, Django
* **Machine Learning:** Scikit-Learn, Pandas, NumPy
* **Frontend:** HTML, CSS, Chart.js
* **Data Source:** Yahoo Finance API

## How to Run Locally
1. Clone the repository.
2. Create and activate a virtual environment.
3. Install dependencies: `pip install django yfinance scikit-learn pandas numpy`
4. Run the development server: `python manage.py runserver`
5. Open `http://127.0.0.1:8000/` in your browser.