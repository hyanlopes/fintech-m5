from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import Address
from .permissions import IsAddressOwner
from .serializers import AddressSerializer


class AddressView(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAddressOwner]

    queryset = Address.objects.all()
    serializer_class = AddressSerializer

    def get_queryset(self):
        if self.request.user.is_superuser:
            return self.queryset.all()

        return self.queryset.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class UpdateDeleteRetrieveView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAddressOwner]

    queryset = Address.objects.all()
    serializer_class = AddressSerializer