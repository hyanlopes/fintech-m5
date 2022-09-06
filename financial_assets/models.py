from django.db import models


class FinancialAssets(models.Models):
    name = models.CharField(max_length=50)
    transaction_type = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_date_time = models.DateTimeField(auto_now=True)
