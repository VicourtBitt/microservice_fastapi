from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.utils.models import StgClient
from app.core.utils.schemas import ClientBase
from app.core.database import get_db
from app.services.client.services import ClientService

router = APIRouter(prefix="/client", tags=["client"])


@router.get("/users")
async def get_users(session: AsyncSession = Depends(get_db)):
    """Get all users"""
    return await ClientService.get_users(session)


@router.get("/users/{user_id}")
async def get_user_by_id(user_id: int, session: AsyncSession = Depends(get_db)):
    """Get user by id"""
    return await ClientService.get_user_by_id(session, user_id)


@router.post("/register", response_model=StgClient)
async def post_client(client: ClientBase, session: AsyncSession = Depends(get_db)):
    """Register a new client"""
    return await ClientService.post_client(session, client)