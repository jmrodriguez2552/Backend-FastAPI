from fastapi import APIRouter, Depends, status, HTTPException
from typing import List
from core.security import get_current_user
from modules.events.event_model import EventModel
from modules.events.event_schema import EventCreateSchema, EventResponseSchema

router = APIRouter(prefix="/events", tags=["Eventos de Agenda"])

@router.get("/", response_model=List[EventResponseSchema])
async def read_events(current_user:dict = Depends(get_current_user)):
    return await EventModel.get_all_by_user(current_user["email"])


@router.post("/", response_model=EventResponseSchema, status_code=status.HTTP_201_CREATED)
async def create_event(event_in:EventCreateSchema, current_user:dict = Depends(get_current_user)):
    return await EventModel.create(event_in.date, event_in.text, current_user["email"])


@router.delete("/{event_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_event(event_id:str, current_user:dict = Depends(get_current_user)):

    success = await EventModel.delete(event_id, current_user["email"])

    if not success:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Evento no encontrado"
        )
    
    return None