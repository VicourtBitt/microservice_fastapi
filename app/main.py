from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.middleware.EncodeMiddleware import Base64Middleware
from app.router.gateway import router as api_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router)
app.add_middleware(Base64Middleware)

@app.on_event("startup")
async def startup():
    from app.core.database import init_db
    await init_db()


@app.on_event("shutdown")
async def shutdown():
    from app.core.database import close_db
    await close_db()