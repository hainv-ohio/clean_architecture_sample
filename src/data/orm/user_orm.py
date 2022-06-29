from sqlalchemy import Table, Column, String, TEXT, BOOLEAN
from core.base.base_sql_orm import BaseSqlOrm, common_columns

from ...domain.entities.user import User

class UserORM(User, BaseSqlOrm):
    __table__ = Table(
        "users",
        BaseSqlOrm.metadata,
        Column("first_name", String(255), nullable=False),
        Column("last_name", String(255), nullable=False),
        Column("phone_number", String(255),
               index=True, nullable=False),
        Column("email", String(255), index=True, nullable=False),
        Column("is_created", BOOLEAN, default=False),
        Column("is_verified", BOOLEAN, default=False),
        Column("profile_image_url", TEXT),
        Column("status", String(50)),
        *common_columns
    )