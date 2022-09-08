import uuid

from django.db import models


class Address(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    zip_code = models.CharField(max_length=8)
    address = models.CharField(max_length=100)
    number = models.IntegerField()
    complement = models.TextField(blank=True, null=True)
    district = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=50)

    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="address"
    )
