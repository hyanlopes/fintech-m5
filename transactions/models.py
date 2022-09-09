import uuid

from django.db import models


class Transaction(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, auto_created=True
    )
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    quantity = models.DecimalField(max_digits=10, decimal_places=10)
    type = models.CharField(max_length=256, default="-")

    wallets = models.ForeignKey(
        "wallets.Wallet", on_delete=models.CASCADE, related_name="transactions"
    )


# Create your models here.
