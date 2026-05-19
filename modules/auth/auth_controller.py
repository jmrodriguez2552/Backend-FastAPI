import jwt
from datetime import datetime, timedelta, timezone
from fastapi import APIRouter, HTTPException, status, Depends
from core.config import SECRET_KEY, ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES
from modules.auth.auth_model import AuthModel
from modules.auth.auth_schema import LoginRequest, TokenResponse, RegistrerRequest
from core.security import get_current_user

# Gestiona la ruta del endpoint que consumirá el formulario de Angular. Si las credenciales son correctas, genera el Token JWT utilizando PyJWT.

router = APIRouter(prefix="/auth", tags=["Autenticación"])

def create_access_token(data:dict):

    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    return jwt.encode(payload=to_encode, key=SECRET_KEY, algorithm=ALGORITHM)


@router.post("/login", response_model=TokenResponse)
async def login(credentials: LoginRequest):
    user = await AuthModel.find_user_by_email(credentials.email)

    if not user or not AuthModel.veerify_password(credentials.password, user["hash_password"]):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Email o contraseña incorrectos")
    
    access_token = create_access_token(data={"sub": user["email"],
                                             "name": user.get("name", ""),
                                             "surname": user.get("surname", ""),
                                             "email": user.get("email", "")})
    
    return {"access_token": access_token, "token_type": "bearer"}

@router.post("/register", status_code=status.HTTP_201_CREATED)
async def register(user_in:RegistrerRequest):

    exist_user = await AuthModel.find_user_by_email(user_in.email)
    if exist_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Correo electrónico ya registrado"
        )
    
    hash_password = AuthModel.get_password_hash(user_in.password)

    user_dict = {
        "name" : user_in.name,
        "surname" : user_in.surname,
        "email" : user_in.email,
        "hash_password": hash_password
    }

    await AuthModel.create_user(user_data=user_dict)

    return {"status": "success", "message": "Empleado registrado correctamente"}

@router.get("/profile")
async def get_profile(current_user: dict = Depends(get_current_user)):
    # Si llega aquí, el token es 100% válido y 'current_user' tiene los datos limpios
    return {
        "message": "Acceso concedido al área privada",
        "user_data": current_user
    }
