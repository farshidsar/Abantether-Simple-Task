
from .base_repository import BaseRepository
from ..models.models import UserWallet

class UserWalletRepository(BaseRepository):
    def __init__(self):
        super().__init__(UserWallet)
