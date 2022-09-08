from rest_framework import generics

from .models import Address
from .serializers import AddressSerializer


class AddressView(generics.ListCreateAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
