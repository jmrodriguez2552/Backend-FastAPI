from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
from core.security import get_current_user
from modules.tasks.task_model import TaskModel
from modules.tasks.task_schema import TaskCreateSchema, TaskUpdateSchema, TaskResponseSchema

router = APIRouter(prefix="/tasks", tags=["Tareas"])

@router.get("/", response_model=List[TaskResponseSchema])
async def read_tasks(current_user: dict = Depends(get_current_user)):
    return await TaskModel.get_all_by_user(current_user["email"])


@router.post("/", response_model=TaskResponseSchema, status_code=status.HTTP_201_CREATED)
async def create_task(task_in: TaskCreateSchema, current_user: dict = Depends(get_current_user)):
    return await TaskModel.create(task_in.title, current_user["email"])


@router.put("/{task_id}", response_model=TaskResponseSchema)
async def update_task(task_id: str, task_in: TaskUpdateSchema, current_user: dict = Depends(get_current_user)):
    updated_task = await TaskModel.update_status(task_id, task_in.completed, current_user["email"])
    if not updated_task:
        raise HTTPException(status_code=404, detail="Tarea no encontrada o no autorizada")
    return updated_task


@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_task(task_id: str, current_user: dict = Depends(get_current_user)):
    success = await TaskModel.delete(task_id, current_user["email"])
    if not success:
        raise HTTPException(status_code=404, detail="Tarea no encontrada o no autorizada")
    return None