import decimal

from django.db.models import Sum

from ..repositories.crypto_repository import CryptoRepository
from ..repositories.transaction_repository import TransactionRepository
from ..repositories.user_repository import UserRepository
from ..repositories.user_wallet_repository import UserWalletRepository
from django.core.exceptions import ObjectDoesNotExist

class TransactionService:
    def __init__(self):
        self.transaction_repository = TransactionRepository()
        self.user_repository = UserRepository()
        self.user_wallet_repository = UserWalletRepository()
        self.crypto_repository = CryptoRepository()
    def buy_crypto(self, user_id, crypto, amount):
        try:
            user = self.user_repository.get_by_id(id=user_id)
        except ObjectDoesNotExist:
            return {'success': False, 'message': 'User not found'}
        decAmount = decimal.Decimal(amount)
        try:
            user_wallet = self.user_wallet_repository.get(user=user, crypto__name='USDT')
        except ObjectDoesNotExist:
            return {'success': False, 'message': 'User wallet not found'}

        if decimal.Decimal(user_wallet.amount) < decAmount * crypto.current_price_usd:
            return {'success': False, 'message': 'Insufficient funds'}


        # Deduct from user wallet
        user_wallet.amount -= decAmount * crypto.current_price_usd
        user_wallet.save()

        # Add crypto to user wallet
        user_crypto_wallet, created = self.user_wallet_repository.get_or_create(user=user, crypto=crypto,amount = 0)
        user_crypto_wallet.amount += decAmount
        user_crypto_wallet.save()

        # Create transaction
        transaction = self.transaction_repository.create(
            user=user,
            crypto=crypto,
            amount=amount,
            is_world_trade=False
        )

        # Check more than 10
        self.check_world_trade()

        return {'success': True, 'message': 'Transaction successful'}

    def check_world_trade(self):
        transactions_by_crypto = (
            self.transaction_repository.filter(is_world_trade=False)
            .values('crypto__name')
            .annotate(total_amount=Sum('amount'))
            .filter(total_amount__gte=10)
        )

        for entry in transactions_by_crypto:
            crypto_name = entry['crypto__name']
            total_amount = entry['total_amount']
            # Update transactions to set is_world_trade to True
            self.transaction_repository.filter(crypto__name=crypto_name, is_world_trade=False).update(is_world_trade=True)
            self.buy_from_exchange(crypto_name, total_amount)



    def buy_from_exchange(self, crypto_name, amount):
        print(f"buy_from_exchange triggered for {crypto_name} with amount {amount}")
