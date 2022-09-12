import uuid

from django.db import models


class Exchange(models.TextChoices):
    BUY = "buy"
    SELL = "sell"


class Transaction(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, auto_created=True
    )
    total_value = models.DecimalField(max_digits=20, decimal_places=8, default=0)
    quantity = models.DecimalField(max_digits=10, decimal_places=8)
    exchange = models.CharField(max_length=50, choices=Exchange.choices)
    quotation = models.DecimalField(max_digits=20, decimal_places=8)
    transaction_date_time = models.DateTimeField(auto_now=True)
    wallets = models.ForeignKey(
        "wallets.Wallet", on_delete=models.CASCADE, related_name="transactions"
    )


# Create your models here.
