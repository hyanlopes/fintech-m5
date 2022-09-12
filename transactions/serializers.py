from django.shortcuts import get_object_or_404
from financial_assets.models import Asset
from rest_framework import serializers

from .models import Transaction


class TransactionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = "__all__"

        read_only_fields = ["quotation", "total_value", "transaction_date_time"]

    # def create(self, validated_data):
    #     financial_assets = get_object_or_404(Asset, id=validated_data["asset_id"])

    total_value = serializers.SerializerMethodField()

    def get_total_value(self, obj):
        return obj.quantity * obj.quotation
