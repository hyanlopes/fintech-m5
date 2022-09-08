from rest_framework import generics

from wallets.models import Wallet
from wallets.serializers import WalletSerializer


class WalletView(generics.ListCreateAPIView):
    serializer_class = WalletSerializer
    queryset = Wallet.objects.all()
