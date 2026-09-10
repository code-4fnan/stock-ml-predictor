import yfinance as yf
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from datetime import datetime, timedelta

def get_prediction(ticker):
    end_date = datetime.now()
    start_date = end_date - timedelta(days=3*365)
    
    # Download historical data
    df = yf.download(ticker, start=start_date, end=end_date, progress=False)
    
    if df.empty:
        return None, None
        
    df['Days'] = np.arange(len(df))
    train_df = df.dropna()
    
    X = train_df[['Days']]
    y = train_df['Close']
    
    # Train the model
    model = LinearRegression()
    model.fit(X, y)
    
    # Predict the next trading day
    next_day = len(df) + 1
    prediction = model.predict([[next_day]])
    
    # Extract values safely using np.ravel
    current_price = float(np.ravel(y.iloc[-1])[0])
    predicted_price = float(np.ravel(prediction)[0])
    
    return current_price, predicted_price