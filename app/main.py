from fastapi import FastAPI
from app.database import init_db
from app.routes import api, views

app = FastAPI(title="To-Do List API")

init_db()
app.include_router(api.router)
app.include_router(views.router)
