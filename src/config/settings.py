from core.config import CoreSettings, CommonApiSettings, SqlDatabaseSettings
from kink import di

"""
Settings for User Management Service
"""
class Settings(CoreSettings, CommonApiSettings, SqlDatabaseSettings):
    USER_API_PREFIX: str = '/user'
    AUTH_API_PREFIX: str = '/auth'

    class Config(object):
        case_sensitive = True


cfg = Settings()

di['cfg'] = cfg
di[Settings] = cfg
di[CoreSettings] = cfg
di[CommonApiSettings] = cfg
di[SqlDatabaseSettings] = cfg