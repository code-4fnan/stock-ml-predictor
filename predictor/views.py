from django.shortcuts import render
from .models import PredictionRecord
from .ml_model import get_prediction

# Top 10 Companies by Market Cap
TICKERS = ["NVDA", "AAPL", "GOOGL", "MSFT", "AMZN", "TSM", "AVGO", "META", "TSLA", "BRK-B"]

def dashboard(request):
    results = []
    
    for ticker in TICKERS:
        current, predicted = get_prediction(ticker)
        
        if current is not None and predicted is not None:
            # Save to MongoDB via Djongo
            PredictionRecord.objects.create(
                ticker=ticker,
                current_price=round(current, 2),
                predicted_price=round(predicted, 2)
            )
            
            results.append({
                'ticker': ticker,
                'current_price': round(current, 2),
                'predicted_price': round(predicted, 2),
                'trend': 'Up' if predicted > current else 'Down'
            })
            
    return render(request, 'dashboard.html', {'results': results})