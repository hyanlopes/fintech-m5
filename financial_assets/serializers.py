from rest_framework import serializers
from wallets.serializers import WalletSerializer

from .api_data import DataCrypto
from .models import Asset


class AssetSerializer(serializers.ModelSerializer):
    # wallets = WalletSerializer(read_only=True, many=True)

    class Meta:
        model = Asset
        fields = "__all__"

        read_only_fields = ["quotation"]

    # real_price = serializers.SerializerMethodField()

    # def get_real_price(self, obj):
    #     return DataCrypto.get()["price_actual"]
