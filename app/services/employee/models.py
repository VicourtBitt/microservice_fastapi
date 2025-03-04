from sqlmodel import Field, SQLModel
from datetime import datetime

class StgEmployee(SQLModel, table=True):
    __tablename__ = "stg_employee"

    employee_id: int = Field(default=None, primary_key=True)
    employee_name: str = Field(default=None)
    employee_email: str = Field(default=None)
    employee_phone: str = Field(default=None)
    last_updated: datetime = Field(default=None)