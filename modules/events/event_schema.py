from pydantic import BaseModel, Field

class EventCreateSchema(BaseModel):
    date:str = Field(..., description="Formato YYYY-MM-DD")
    text:str = Field(..., min_length=3, max_length=150)

class EventResponseSchema(BaseModel):
    id:str
    date:str
    text:str

    class Config:
        from_attributes = True
