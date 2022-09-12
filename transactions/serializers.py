from django.shortcuts import get_object_or_404
from rest_framework import serializers

from .models import Transaction


class AssetNotExistError(Exception):
    pass


class TransactionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = "__all__"

        read_only_fields = ["quotation", "total_value", "transaction_date_time"]

    total_value = serializers.SerializerMethodField()

    def get_total_value(self, obj):

        # if "quotation" in obj:
        if obj.quotation:
            return float(obj.quantity) * float(obj.quotation)
        else:
            raise AssetNotExistError("The asset ticket not exist in database")

    def create(self, validated_data):

        if "quotation" in validated_data:
            validated_data["total_value"] = float(validated_data["quantity"]) * float(
                validated_data["quotation"]
            )

            return Transaction.objects.create(**validated_data)
