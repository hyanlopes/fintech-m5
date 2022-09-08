from rest_framework import serializers

from .models import Asset

#from wallets.serializers import WalletSerializer
 
 
 
class AssetSerializer(serializers.ModelSerializer):
    class Meta:
       model = Asset
       fields = "__all__"
    

