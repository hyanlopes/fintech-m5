from django.db import models


class Exchange(models.TextChoices):
   BUY = "buy"
   SELL = "sell"
   DEFAULT = "none"
 
class Asset(models.Models):
   name = models.CharField(max_length=50)
   transaction_type = models.CharField(max_length=50, choices=Exchange.choices, default=Exchange.DEFAULT)
   price = models.DecimalField(max_digits=15, decimal_places=2)
   transaction_date_time = models.DateTimeField(auto_now=True)
 
   wallets = models.ManyToManyField("wallets.Wallet", related_name="assets")
   #wallets = models.ForeignKey("wallets.Wallet", on_delete=models.CASCADE, related_name="assets")
