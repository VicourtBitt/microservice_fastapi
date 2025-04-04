from sqlalchemy.ext.asyncio import AsyncSession
from sqlmodel import select
from app.core.utils.models import StgClient

class ClientRepository:
    @staticmethod
    async def get_users(session: AsyncSession):
        result = await session.execute(select(StgClient))
        return result.scalars().all()
    

    @staticmethod
    async def get_user_by_id(session: AsyncSession, user_id: int):
        result = await session.execute(select(StgClient).where(StgClient.client_id == user_id))
        return result.scalars().first()
    

    @staticmethod
    async def post_client(session: AsyncSession, client):
        new_client = StgClient(
            client_id=client.client_id,
            client_attendant_id=client.client_attendant_id,
            client_name=client.client_name,
            client_email=client.client_email,
            client_phone=client.client_phone,
            last_updated=client.last_updated
        )
        
        session.add(new_client)
        await session.commit()
        await session.refresh(new_client)
        return new_client