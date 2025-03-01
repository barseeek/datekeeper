from fastapi import APIRouter

router = APIRouter()


@router.get('/')
async def debug():
    return {'message': 'Hello World'}
