from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from transactions.api_data import DataCrypto

from wallets.models import Wallet
from wallets.serializers import WalletSerializer


class WalletView(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    serializer_class = WalletSerializer
    queryset = Wallet.objects.all()

    def perform_create(self, serializer):

        crypto_is_valid = DataCrypto.get(crypto=self.request.data["asset_ticket"])

        serializer.save(user=self.request.user)
