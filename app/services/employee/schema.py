from pydantic import BaseModel
from typing import Optional

class EmployeeBase(BaseModel):
    employee_id: Optional[int] = None
    employee_name: Optional[str] = None
    employee_email: Optional[str] = None
    employee_phone: Optional[str] = None
    last_updated: Optional[str] = None