from ..models.models import User, UserWallet
from ..repositories.user_repository import UserRepository
from ..repositories.user_wallet_repository import UserWalletRepository


class UserWalletService:
    def __init__(self):
        self.user_repository = UserRepository()
        self.user_wallet_repository = UserWalletRepository()
    def get_user_wallet(self, user_id):
        try:
            user = self.user_repository.get_by_id(id=user_id)
            user_wallets = self.user_wallet_repository.filter(user=user)
            return user_wallets
        except User.DoesNotExist:
            return None
