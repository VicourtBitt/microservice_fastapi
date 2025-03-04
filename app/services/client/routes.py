from fastapi import APIRouter, Depends
from sqlmodel import Session, select
from typing import List
from ...core.database import get_db
from .models import StgClient
from .schema import ClientBase

## Initialize router for each client route
router = APIRouter()


## Get all clients
@router.get("/all", response_model=List[StgClient])
def get_all_clients(db: Session = Depends(get_db)):
    statement = select(
        StgClient
    )

    clients = db.exec(statement)
    return clients


## Get client by ID
@router.get("/{client_id}", response_model=StgClient)
def get_client_by_id(client_id: int, db: Session = Depends(get_db)):
    statement = select(
        StgClient
    ).where(
        StgClient.client_id == client_id
    )

    client = db.exec(statement).first()
    return client


## Post client
@router.post("/register", response_model=StgClient)
def post_client(client: ClientBase, db: Session = Depends(get_db)):
    new_client = StgClient(
        client_id=client.client_id,
        client_attendant_id=client.client_attendant_id,
        client_name=client.client_name,
        client_email=client.client_email,
        client_phone=client.client_phone,
        last_updated=client.last_updated
    )

    db.add(new_client)
    db.commit()
    db.refresh(new_client)
    return new_client