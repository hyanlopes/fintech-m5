from rest_framework import serializers
from transactions.models import Transaction
from transactions.serializers import TransactionsSerializer

from .models import Wallet


class WalletSerializer(serializers.ModelSerializer):
    transactions = TransactionsSerializer(many=True, read_only=True)

    class Meta:
        model = Wallet
        fields = "__all__"
        depth = 1

    def create(self, validated_data):
        wallet = Wallet.objects.create(**validated_data)

        return wallet
