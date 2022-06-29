from datetime import datetime
from typing import Dict
"""
Just control the dependencies of Entities here
"""
class BaseEntity(object):
    ...

    def to_json(self) -> Dict:
        return {k: v for k, v in self.__dict__.items() if not '__' in k}

"""
Common Entitity with common fields
"""
class CommonEntity(BaseEntity):
    id: str
    created_at: datetime
    created_by: str
    updated_at: datetime
    updated_by: str
    is_deleted: bool
    deleted_at: datetime
    deleted_by: str

    # def to_json(self) -> Dict:
    #     return {
    #         'created_at': self.created_at,
    #         'created_by': self.created_by,
    #         'updated_at': self.updated_at,
    #         'updated_by': self.updated_by,
    #         'is_deleted': self.is_deleted,
    #         'deleted_at': self.deleted_at,
    #         'deleted_by': self.deleted_by,
    #         **super().to_json()
    #     }

