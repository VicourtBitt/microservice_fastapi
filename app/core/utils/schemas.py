from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class EmployeeBase(BaseModel):
    employee_id: Optional[int] = None
    employee_name: Optional[str] = None
    employee_email: Optional[str] = None
    employee_phone: Optional[str] = None
    last_updated: Optional[datetime] = None


class ClientBase(BaseModel):
    client_id: Optional[int] = None
    client_attendant_id: Optional[int] = None
    client_name: Optional[str] = None
    client_email: Optional[str] = None
    client_phone: Optional[str] = None
    last_updated: Optional[datetime] = None


class UserLoginBase(BaseModel):
    user_id: Optional[int] = None
    user_email: Optional[str] = None
    user_hash: Optional[str] = None
    is_active: Optional[bool] = None
    last_updated: Optional[datetime] = None


class TransactionBase(BaseModel):
    transaction_id: Optional[int] = None
    account_id: Optional[int] = None
    transaction_amount: Optional[float] = None
    transaction_type: Optional[str] = None
    transaction_date: Optional[datetime] = None
    last_updated: Optional[datetime] = None


class ClientAccountBase(BaseModel):
    account_id: Optional[int] = None
    client_id: Optional[int] = None
    account_balance: Optional[float] = None
    is_current: Optional[bool] = None
    registered_at: Optional[datetime] = None
    last_updated: Optional[datetime] = None


class JWTBase(BaseModel):
    jwt_id: Optional[int] = None
    user_id: Optional[int] = None
    jwt_refresh_token: Optional[str] = None
    # access_token: Optional[str] = None
    jwt_refresh_expiration: Optional[datetime] = None