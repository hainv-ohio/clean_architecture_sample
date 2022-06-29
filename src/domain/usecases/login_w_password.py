from .base import BaseUserUsecase
from typing import Tuple
from ..entities.user import User

class RegisterWithPassword(BaseUserUsecase):
    async def execute(self, email, password) -> Tuple[User, Failure]:
        if len(password) < 6:
            return None, Failure("Password must ...")
        return await self.repository.login_w_password(email, password)