import uuid

from django.db import models


class Wallet(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    name = models.CharField(max_length=50)

    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="wallets"
    )

    financial_assets = models.ManyToManyField(
        "financial_assets.Asset", related_name="financial_assets"
    )

    extract = models.OneToOneField("extracts.Extract", on_delete=models.CASCADE)
