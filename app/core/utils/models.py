from sqlmodel import Field, SQLModel
from datetime import datetime

class StgClient(SQLModel, table=True):
    __tablename__ = "stg_client"

    client_id: int = Field(default=None, primary_key=True, index=True)
    client_attendant_id: int = Field(default=None)
    client_name: str = Field(default=None)
    client_email: str = Field(default=None)
    client_phone: str = Field(default=None)
    last_updated: datetime = Field(default=datetime.now())


class StgEmployee(SQLModel, table=True):
    __tablename__ = "stg_employee"

    employee_id: int = Field(default=None, primary_key=True, index=True)
    employee_name: str = Field(default=None)
    employee_email: str = Field(default=None)
    employee_phone: str = Field(default=None)
    last_updated: datetime = Field(default=datetime.now())


class DimUserLogin(SQLModel, table=True):
    __tablename__ = "dim_user_login"

    user_id: int = Field(default=None, primary_key=True, index=True)
    user_email: str = Field(default=None)
    user_hash: str = Field(default=None)
    is_active: bool = Field(default=True)
    last_updated: datetime = Field(default=datetime.now())


class DimClientAccount(SQLModel, table=True):
    __tablename__ = "dim_client_account"

    account_id: int = Field(default=None, primary_key=True, index=True)
    client_id: int = Field(default=None)
    account_balance: float = Field(default=0.0)
    is_current: bool = Field(default=True)
    registered_at: datetime = Field(default=datetime.now())
    last_updated: datetime = Field(default=datetime.now())


class DimJsonWebTokens(SQLModel, table=True):
    __tablename__ = "dim_json_web_tokens"

    token_id: int = Field(default=None, primary_key=True, index=True)
    user_id: int = Field(default=None)
    jwt_refresh_token: str = Field(default=None)
    jwt_refresh_expiration: datetime = Field(default=datetime.now())