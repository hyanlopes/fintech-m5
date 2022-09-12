from django.shortcuts import get_object_or_404
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
        # import ipdb

        # ipdb.set_trace()

        return float(obj.quantity) * float(obj.quotation)

    def create(self, validated_data):
        validated_data["total_value"] = float(validated_data["quantity"]) * float(
            validated_data["quotation"]
        )

        return Transaction.objects.create(**validated_data)
