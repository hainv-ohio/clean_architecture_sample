
from kink import di

from src.domain.repository import UserRepository
from src.data.repository import UserRepositoryImpl

async def init_di():
    repository =  UserRepositoryImpl()
    await repository.init()

    di[UserRepository] = repository
