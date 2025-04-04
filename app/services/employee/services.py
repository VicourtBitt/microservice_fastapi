from sqlalchemy.ext.asyncio import AsyncSession
from app.services.employee.repository import EmployeeRepository

class EmployeeService:
    @staticmethod
    async def get_employees(session: AsyncSession):
        """Get all employees"""
        return await EmployeeRepository.get_employees(session)
    
    
    @staticmethod
    async def get_employee_by_id(session: AsyncSession, employee_id: int):
        """Get employee by id"""
        return await EmployeeRepository.get_employee_by_id(session, employee_id)
    

    @staticmethod
    async def post_employee(session: AsyncSession, employee):
        """Register a new employee"""
        return await EmployeeRepository.post_employee(session, employee)