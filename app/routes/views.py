from fastapi import APIRouter, Request, Form
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from app import crud
from app.models import TaskCreate

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")

@router.get("/")
def home(request: Request):
    tasks = crud.get_tasks()
    return templates.TemplateResponse("tasks.html", {"request": request, "tasks": tasks})

@router.get("/add")
def add_form(request: Request):
    return templates.TemplateResponse("add_task.html", {"request": request})

@router.post("/add")
def add_task(title: str = Form(...), description: str = Form(None), due_date: str = Form(None)):
    crud.create_task(TaskCreate(title=title, description=description, due_date=due_date))
    return RedirectResponse("/", status_code=302)
