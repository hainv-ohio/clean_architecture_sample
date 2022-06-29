from .base import BaseUserUsecase
from typing import Tuple

from core.types import Failure
from ..entities.user import User


class GetUserByEmail(BaseUserUsecase):
    async def execute(self, email, *args, **kwargs) -> Tuple[User, Failure]:
        return await self.repository.get_user_by_email(email)