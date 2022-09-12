import uuid

from django.db import models


class Wallet(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    name = models.CharField(max_length=50)
    asset_ticket = models.CharField(max_length=10)

    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="wallets"
    )
