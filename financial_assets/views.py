from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from wallets.models import Wallet

from .models import Asset
from .serializers import AssetSerializer
from .permissions import AssetPermissionsCustom


class ListCreateAssetView(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = AssetSerializer

    def perform_create(self, serializer):
        wallet = get_object_or_404(Wallet, pk=self.pk)

        self.check_object_permissions(self.request, wallet)
        serializer.save(wallet=wallet)


    def get_queryset(self):
        wallet = get_object_or_404(Wallet, pk=self.pk)
        assets = Asset.objects.filter(wallet=wallet)

        return assets


class RetrieveUpdateAssetView(generics.RetrieveUpdateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    serializer_class = AssetSerializer
