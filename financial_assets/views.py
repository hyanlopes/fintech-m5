from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from users.permissions import IsOwnerPermission
from wallets.models import Wallet

from .models import Asset
from .serializers import AssetSerializer


class ListCreateAssetView(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsOwnerPermission]
    serializer_class = AssetSerializer

    def perform_create(self, serializer):
        wallet = get_object_or_404(Wallet, pk=self.kwargs["wallets_id"])
        
        self.check_object_permissions(self.request, wallet)
        serializer.save(wallet=wallet)

    def get_queryset(self):
        wallet = get_object_or_404(Wallet, pk=self.kwargs["wallets_id"])
        assets = Asset.objects.filter(wallet=wallet)

        return assets 


class RetrieveUpdateAssetView(generics.RetrieveUpdateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsOwnerPermission]
    queryset = Asset.objects.all()
    serializer_class = AssetSerializer
