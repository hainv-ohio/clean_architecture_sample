from sqlalchemy.dialects import postgresql as psql
from sqlalchemy import ForeignKey, Column, BOOLEAN, TIMESTAMP, text,  inspect
from sqlalchemy.sql import func
from sqlalchemy.ext.declarative import (
    declarative_base,
)

BaseSqlOrm = declarative_base()

def get_common_id_column():
    return Column("id", psql.UUID(as_uuid=True),
            server_default=text('gen_random_uuid()'),
            primary_key=True,
            index=True
           )

def get_fk_column(col_name: str, f_table_name: str, f_col_name: str,*args, **kwargs):
    fk = f_table_name+'.'+f_col_name
    return Column(col_name, psql.UUID(as_uuid=True), ForeignKey(fk), *args, **kwargs)

def get_common_columns ():
    return [
        Column("created_at", TIMESTAMP(timezone=False), server_default=func.now()),
        get_fk_column("created_by", "users", "id"),
        Column("updated_at", TIMESTAMP(timezone=False), onupdate=func.now()),
        get_fk_column("updated_by",  "users", "id"),
        Column("deleted_at", TIMESTAMP(timezone=False)),
        get_fk_column("deleted_by",  "users", "id"),
        Column("is_deleted", BOOLEAN, default=False)
    ]