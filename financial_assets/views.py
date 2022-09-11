from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
#from users.permissions import IsOwnerPermission
from wallets.models import Wallet

from .api_data import DataCrypto
from .models import Asset
from .permissions import IsWalletOwner, IsWalletOwnerOrAdmin
from .serializers import AssetSerializer


class ListCreateAssetView(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsWalletOwner]
    serializer_class = AssetSerializer
    queryset = Asset.objects.all()

    """ def perform_create(self, serializer):
        wallet = get_object_or_404(Wallet, pk=self.kwargs["wallets_id"])
        self.check_object_permissions(self.request, wallet)
        serializer.save(wallet=self.request.wallets) """

    """ def get_queryset(self):
        wallet = get_object_or_404(Wallet, pk=self.kwargs["wallets_id"])
        assets = Asset.objects.filter(wallet=wallet)
        return assets """


class RetrieveUpdateAssetView(generics.RetrieveUpdateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsWalletOwnerOrAdmin, IsWalletOwner]
    queryset = Asset.objects.all()
    serializer_class = AssetSerializer

    lookup_url_kwarg = "assets_id"
