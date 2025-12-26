from fastapi import APIRouter, HTTPException
from app.models import TaskCreate
from app import crud

router = APIRouter(prefix="/api/tasks", tags=["Tasks"])

@router.post("/")
def create(task: TaskCreate):
    crud.create_task(task)
    return {"message": "Task created"}

@router.get("/")
def read_all():
    return crud.get_tasks()

@router.get("/{task_id}")
def read_one(task_id: int):
    task = crud.get_task(task_id)
    if not task:
        raise HTTPException(404, "Task not found")
    return task

@router.put("/{task_id}")
def update(task_id: int, task: TaskCreate):
    if not crud.update_task(task_id, task):
        raise HTTPException(404, "Task not found")
    return {"message": "Task updated"}

@router.delete("/{task_id}")
def delete(task_id: int):
    if not crud.delete_task(task_id):
        raise HTTPException(404, "Task not found")
    return {"message": "Task deleted"}
