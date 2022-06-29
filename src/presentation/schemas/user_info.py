from pydantic import BaseModel
from .base import BaseResponseSchema
from ...domain.entities.user import User

class UserInfoSchema(BaseModel):
    first_name: str
    last_name: str
    phone_number: str
    email: str
    is_created: bool = True
    is_verified: bool = False
    profile_image_url: str = ""
    status: str

    class Config:
        schema_extra = {
            "example": {
                "first_name": "Henry",
                "last_name": "Nguyen",
                "phone_number": "0987654321",
                "email": "example@higate.com",
                "is_created": True,
                "is_verified": False,
                "profile_image_url": "",
                "status": "ACTIVE"
            }
        }


class  UserInfoResponse(BaseResponseSchema):
    data: UserInfoSchema

    class Config:
        schema_extra = {
            "example": {
                "status": "Success",
                "message": "Success",
                "data": UserInfoSchema.Config.schema_extra['example']
            }
        }