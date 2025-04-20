from fastapi import FastAPI
from app.core.middleware.EncodeMiddleware import Base64Middleware
from app.router.gateway import router as api_router

app = FastAPI()
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


@app.get("/")
async def root():
    return {"message": "Welcome to the FastAPI application!"}