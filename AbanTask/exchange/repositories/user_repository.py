
from .base_repository import BaseRepository
from ..models.models import User

class UserRepository(BaseRepository):
    def __init__(self):
        super().__init__(User)
