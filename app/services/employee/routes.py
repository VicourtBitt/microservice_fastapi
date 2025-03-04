from fastapi import APIRouter, Depends
from sqlmodel import Session, select
from typing import List
from ...core.database import get_db
from .models import StgEmployee
from .schema import EmployeeBase

## Initialize router for each employee route
router = APIRouter()


## Get all employees
@router.get("/all", response_model=List[StgEmployee])
def get_all_employees(db: Session = Depends(get_db)):
    statement = select(
        StgEmployee
    ).select_from(
        StgEmployee
    )

    employees = db.exec(statement)
    return employees


## Get employee by ID
@router.get("/{employee_id}", response_model=StgEmployee)
def get_employee_by_id(employee_id: int, db: Session = Depends(get_db)):
    statement = select(
        StgEmployee
    ).where(
        StgEmployee.employee_id == employee_id
    )

    employee = db.exec(statement).first()
    return employee


## Post employee
@router.post("/register", response_model=StgEmployee)
def post_employee(employee: EmployeeBase, db: Session = Depends(get_db)):
    new_employee = StgEmployee(
        employee_id=employee.employee_id,
        employee_name=employee.employee_name,
        employee_email=employee.employee_email,
        employee_phone=employee.employee_phone,
        last_updated=employee.last_updated
    )

    db.add(new_employee)
    db.commit()
    db.refresh(new_employee)
    return new_employee