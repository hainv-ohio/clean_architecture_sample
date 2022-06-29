
from domain.repository import UserRepository

class MockUserRepository(UserRepository):
    def login_w_password(self, email, password) -> Tuple[User, Failure]:
        return 