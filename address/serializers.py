from rest_framework.serializers import ModelSerializer

from .models import Address


class AddressSerializer(ModelSerializer):
    class Meta:
        models = Address
        fields = "__all__"
