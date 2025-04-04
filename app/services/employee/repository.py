from sqlalchemy.ext.asyncio import AsyncSession
from sqlmodel import select
from app.core.utils.models import StgEmployee

class EmployeeRepository:
    @staticmethod
    async def get_employees(session: AsyncSession):
        result = await session.execute(select(StgEmployee))
        return result.scalars().all()
    

    @staticmethod
    async def get_employee_by_id(session: AsyncSession, employee_id: int):
        result = await session.execute(select(StgEmployee).where(StgEmployee.employee_id == employee_id))
        return result.scalars().first()
    
    
    @staticmethod
    async def post_employee(session: AsyncSession, employee):
        new_employee = StgEmployee(
            employee_id=employee.employee_id,
            employee_name=employee.employee_name,
            employee_email=employee.employee_email,
            employee_phone=employee.employee_phone,
            last_updated=employee.last_updated
        )
        
        session.add(new_employee)
        await session.commit()
        await session.refresh(new_employee)
        return new_employee