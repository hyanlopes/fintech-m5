from rest_framework.serializers import ModelSerializer

from .models import Address


class AddressSerializer(ModelSerializer):
    class Meta:
        model = Address
        fields = "__all__"
        read_only_fields = ["user"]
        depth = 1
