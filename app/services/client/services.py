from sqlalchemy.ext.asyncio import AsyncSession
from app.services.client.repository import ClientRepository

class ClientService:
    @staticmethod
    async def get_users(session: AsyncSession):
        return await ClientRepository.get_users(session)
    

    @staticmethod
    async def get_user_by_id(session: AsyncSession, user_id: int):
        return await ClientRepository.get_user_by_id(session, user_id)
    

    @staticmethod
    async def post_client(session: AsyncSession, client):
        return await ClientRepository.post_client(session, client)