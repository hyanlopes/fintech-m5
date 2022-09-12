from django.shortcuts import get_object_or_404
from financial_assets.api_data import DataCrypto
from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

# from users.permissions import IsOwnerPermission
from wallets.models import Wallet

from .models import Transaction
from .serializers import TransactionsSerializer


class ListCreateTransactionView(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = TransactionsSerializer
    queryset = Transaction.objects.all()

    def perform_create(self, serializer):
        crypto_quotation = DataCrypto.get(crypto="ETH")["price_actual"]
        serializer.save(quotation=crypto_quotation)
