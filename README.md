# 📈 Stock Market ML Predictor

A web application that predicts the next-day closing price of the Top 10 companies by market capitalization using Machine Learning, with predictions securely logged in a NoSQL cloud database.

## Features
* **Live Data Ingestion:** Automatically downloads the last 3 years of daily historical closing prices using `yfinance`.
* **On-the-Fly Machine Learning:** Trains a fresh Linear Regression model via `scikit-learn` for each company upon page load.
* **Dynamic Visualization:** Uses `Chart.js` to render a comparative bar graph of current vs. predicted prices.
* **Cloud Database Persistence:** Securely connects to MongoDB Atlas to store and track prediction records over time.

## Tech Stack
* **Backend:** Python, Django
* **Database:** MongoDB Atlas, Djongo, PyMongo
* **Machine Learning:** Scikit-Learn, Pandas, NumPy
* **Frontend:** HTML, CSS, Chart.js
* **Data Source:** Yahoo Finance API

## How to Run Locally
1. Clone the repository.
2. Create and activate a virtual environment.
3. Install dependencies: `pip install django yfinance scikit-learn pandas numpy djongo pymongo dnspython certifi`
4. Configure your MongoDB Atlas connection string in `settings.py`.
5. Run the database migrations:
   ```bash
   python manage.py makemigrations
   python manage.py migrate