from fastapi import FastAPI

from app.routers import router

app = FastAPI()

app.include_router(router=router, prefix='/api/v1', tags=['users'])
