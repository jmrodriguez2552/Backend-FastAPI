from pydantic import BaseModel, EmailStr, Field

# Define los datos que viajan entre Angular y FastAPI.

class LoginRequest(BaseModel):
    email: EmailStr
    password: str = Field(..., min_length=6, max_length=72)


class TokenResponse(BaseModel):
    access_token : str
    token_type: str = "bearer"


class RegistrerRequest(BaseModel):
    name: str = Field(..., min_length=3, max_length=50)
    surname:str = Field(..., min_length=3, max_length=50)
    email:EmailStr
    password:str = Field(..., min_length=6, max_length=72)
