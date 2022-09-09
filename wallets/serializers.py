from extracts.models import Extract
from extracts.serializers import ExtractSerializer
from rest_framework import serializers

from .models import Wallet


class WalletSerializer(serializers.ModelSerializer):
    extract = ExtractSerializer(read_only=True)

    class Meta:
        model = Wallet
        fields = [
            "id",
            "name",
        ]

    def create(self, validated_data):
        extract = Extract.objects.create()
        wallet = Wallet.objects.create(**validated_data, extract=extract)

        return wallet
