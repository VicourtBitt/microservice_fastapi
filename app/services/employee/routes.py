from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.utils.models import StgEmployee
from app.core.utils.schemas import EmployeeBase
from app.core.database import get_db
from app.services.employee.services import EmployeeService

router = APIRouter(prefix="/employee", tags=["employee"])

@router.get("/employees")
async def get_employees(session: AsyncSession = Depends(get_db)):
    """Get all employees"""
    return await EmployeeService.get_employees(session)


@router.get("/employees/{employee_id}")
async def get_employee_by_id(employee_id: int, session: AsyncSession = Depends(get_db)):
    """Get employee by id"""
    return await EmployeeService.get_employee_by_id(session, employee_id)


@router.post("/register", response_model=StgEmployee)
async def post_employee(employee: EmployeeBase, session: AsyncSession = Depends(get_db)):
    """Register a new employee"""
    return await EmployeeService.post_employee(session, employee)