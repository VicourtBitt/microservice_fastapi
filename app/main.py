from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .services.client.routes import router as client
from .services.employee.routes import router as employee

# Initialize FastAPI app
app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include/Import routes
app.include_router(client, prefix="/client", tags=["client"])
app.include_router(employee, prefix="/employee", tags=["employee"])