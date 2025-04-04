from fastapi import APIRouter
from app.services.client.routes import router as client_router
from app.services.employee.routes import router as employee_router

router = APIRouter(prefix="/api/v1")

router.include_router(client_router)
router.include_router(employee_router)
