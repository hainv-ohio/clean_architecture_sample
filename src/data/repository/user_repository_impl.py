import traceback

from loguru import logger
from typing import Tuple

from core.types import Failure
from core.modules.sql_module import create_database_tables

from ...domain.repository import UserRepository
from ...domain.entities.user import User
from ..dao.user_dao import UserDAO


class UserRepositoryImpl(UserRepository):
    def __init__(self) -> None:
        super().__init__()
        self.user_dao = UserDAO()

    async def init(self):
        await create_database_tables()

    async def get_user_by_email(self, email) -> Tuple[User, Failure]:
        try:
            result = await self.user_dao.find_one(email=email)
            return result, None
        except:
            logger.error(f'Error {traceback.format_exc()}')
            return None, Failure(404, "Not found")
