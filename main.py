from fastapi import FastAPI

from api.router import api_router
from db.tortoise_config import init_db

app = FastAPI()

app.include_router(api_router)

@app.on_event("startup")
async def startup_event():
    await init_db()
