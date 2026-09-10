from django.db import models

class PredictionRecord(models.Model):
    ticker = models.CharField(max_length=10)
    current_price = models.FloatField()
    predicted_price = models.FloatField()
    prediction_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.ticker} - Predicted: ${self.predicted_price}"