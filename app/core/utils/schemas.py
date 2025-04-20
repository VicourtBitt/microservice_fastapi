from pydantic import BaseModel
from typing import Optional


class EmployeeBase(BaseModel):
    employee_id: Optional[int] = None
    employee_name: Optional[str] = None
    employee_email: Optional[str] = None
    employee_phone: Optional[str] = None
    last_updated: Optional[str] = None


class ClientBase(BaseModel):
    client_id: Optional[int] = None
    client_attendant_id: Optional[int] = None
    client_name: Optional[str] = None
    client_email: Optional[str] = None
    client_phone: Optional[str] = None
    last_updated: Optional[str] = None