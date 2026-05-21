from pydantic import BaseModel

class ManualResponseSchema(BaseModel):
    id:str
    code:str
    title:str
    version:str
    departament:str
    pdf_url:str

    class Config:
        from_attributes = True