import uuid

from django.db import models


class Wallet(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    name = models.CharField(max_length=50)
    wallet_id = models.ManyToManyField(
        "financial_assets.FinancialAssets", related_name="financial_assets"
    )
