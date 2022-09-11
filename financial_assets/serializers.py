from rest_framework import serializers

from .api_data import DataCrypto
from .models import Asset

#from wallets.serializers import WalletSerializer



class AssetSerializer(serializers.ModelSerializer):
    class Meta:
       model = Asset
       fields = "__all__"
    real_price = serializers.SerializerMethodField()

    def get_real_price(self, obj):
        return DataCrypto.get()["price_actual"]
