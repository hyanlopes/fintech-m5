from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import Response

# from users.permissions import IsOwnerPermission
from wallets.models import Wallet

from .api_data import DataCrypto
from .models import Transaction
from .serializers import TransactionsSerializer


class ListCreateTransactionView(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = TransactionsSerializer
    queryset = Transaction.objects.all()

    def perform_create(self, serializer):

        wallet = get_object_or_404(Wallet, id=self.request.data["wallets"])

        try:
            crypto_quotation = DataCrypto.get(crypto=wallet.asset_ticket)[
                "price_actual"
            ]

            if crypto_quotation != None:
                serializer.save(quotation=crypto_quotation)

        except KeyError as err:
            return Response({"error": err.args[0]}, status=404)
