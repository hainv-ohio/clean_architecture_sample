
from abc import abstractmethod
from typing import Tuple
from core.base import BaseRepository
from core.types import Failure
from domain import repository
from ..entities.user import User

class UserRepository(BaseRepository):
    @abstractmethod
    async def get_user_by_email(self, email, *args, **kwargs) -> Tuple[User, Failure]: raise NotImplementedError
    
    @abstractmethod
    async def login_w_password(self, email, password) -> Tuple[User, Failure]: raise NotImplementedError


