
from kink import inject

from core.base import BaseUseCase
from ..repository import UserRepository

@inject
class BaseUserUsecase(BaseUseCase):
    def __init__(self, repository: UserRepository) -> None:
        self.repository = repository