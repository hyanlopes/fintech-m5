import uuid

from django.db import models


class Wallet(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    name = models.CharField(max_length=50)

    # FK 1:N - users
    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="wallets"
    )

    # FK N:N - financial assets
    # financial_assets = models.ManyToManyField(
    #     "financial_assets.FinancialAssets", related_name="financial_assets"
    # )
