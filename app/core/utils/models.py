from sqlmodel import Field, SQLModel
from datetime import datetime

class StgClient(SQLModel, table=True):
    __tablename__ = "stg_client"

    client_id: int = Field(default=None, primary_key=True)
    client_attendant_id: int = Field(default=None)
    client_name: str = Field(default=None)
    client_email: str = Field(default=None)
    client_phone: str = Field(default=None)
    last_updated: datetime = Field(default=None)


class StgEmployee(SQLModel, table=True):
    __tablename__ = "stg_employee"

    employee_id: int = Field(default=None, primary_key=True)
    employee_name: str = Field(default=None)
    employee_email: str = Field(default=None)
    employee_phone: str = Field(default=None)
    last_updated: datetime = Field(default=None)