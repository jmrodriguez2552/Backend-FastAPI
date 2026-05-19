from pydantic import BaseModel, Field
from typing import Optional

# Lo que se recibe de Angular a FastApi
class TaskCreateSchema(BaseModel):
    title: str = Field(..., min_length=3, max_length=100)

# Cuando se actualiza la tarea 
class TaskUpdateSchema(BaseModel):
    completed:bool

#La respuesta que se envía a Angular
class TaskResponseSchema(BaseModel):
    id: str # id de mongoDB
    title:str
    completed:bool

    # Permite mapear los atributos directamente desde diccionarios de Python
    class Config:
        from_attributes = True