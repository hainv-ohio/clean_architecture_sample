
from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse

from ...domain.usecases.get_user_by_email import GetUserByEmail

from ..schemas.user_info import UserInfoResponse
from ..schemas.base import BaseResponseSchema

router = APIRouter()


@router.get("/info",
            name="Get user info by email",
            description='Get user info by email',
            response_model=UserInfoResponse,
            responses={
                 400: {"model": BaseResponseSchema},
                 401: {"model": BaseResponseSchema}
            })
async def get_user_by_email(email: str,
                            get_user_by_email_usecase: GetUserByEmail = Depends(lambda: GetUserByEmail())):
    result, failure = await get_user_by_email_usecase.execute(email)
    if failure is not None:
        return JSONResponse({
            'status': 'failed', 
            'message': 'failed',
            'data': failure.message
        },
        status_code=failure.code)
    return {
        'status': 'success', 
        'message': 'success',
        'data': result.to_json()
    }
