from typing import Any, Dict

from pydantic import BaseSettings, PostgresDsn, validator

"""
Settings for:
- Logging system
- Service name & Version
"""
from dotenv import load_dotenv
load_dotenv('./services/user_management_service/.env')
class SqlDatabaseSettings(BaseSettings):
    DB_HOST: str = ''
    DB_PORT: str = ''
    DB_USER: str = ''
    DB_PASSWORD: str = ''
    DB_NAME: str = ''
    DATABASE_URI: PostgresDsn = None

    @validator('DATABASE_URI', pre=True)
    def assemble_db_connection(
        cls, value: str, values: Dict[str, Any],  # noqa: N805, WPS110
    ) -> str:
        if isinstance(value, str) and not value == '' and not value is None:
            return value

        return PostgresDsn.build(
            scheme='postgresql+asyncpg',
            user=values.get('DB_USER'),
            password=values.get('DB_PASSWORD'),
            host=values.get('DB_HOST'),
            port=values.get('DB_PORT'),
            path='/{0}'.format(values.get('DB_NAME')),
        )

    class Config(object):
        case_sensitive = True

