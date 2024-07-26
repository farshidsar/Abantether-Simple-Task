
from .base_repository import BaseRepository
from ..models.models import Transaction

class TransactionRepository(BaseRepository):
    def __init__(self):
        super().__init__(Transaction)
