from rest_framework import serializers
from models.models import UserWallet, Crypto, Transaction

class CryptoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Crypto
        fields = ['name', 'current_price_usd']

class UserWalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserWallet
        fields = ['user', 'crypto', 'amount']

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ['user', 'crypto', 'amount', 'is_world_trade', 'created_at']
