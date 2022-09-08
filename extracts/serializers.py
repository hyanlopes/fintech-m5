from rest_framework import serializers

from .models import Extract
from financial_assets.models import Asset

from django.shortcuts import get_object_or_404

class ExtractSerializer(serializers.ModelSerializer):
    class Meta:
       model = Extract
       fields = "__all__"

    def create(self, validated_data):
        financial_assets = get_object_or_404(Asset,id=validated_data['asset_id'])




