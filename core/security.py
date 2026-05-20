import jwt
from fastapi import HTTPException, status, Depends
from fastapi.security import OAuth2PasswordBearer, APIKeyHeader
from core.config import SECRET_KEY, ALGORITHM

# Validador de Tokens
# Define de dónde sacará FastAPI el token. 
# Angular enviará el token en la cabecera: Authorization: Bearer <TOKEN>
oauth2_scheme = APIKeyHeader(name="Authorization", auto_error=False)

async def get_current_user(token: str = Depends(oauth2_scheme)) -> dict: # Dependencia para validar el JWT

    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="No se pudieron validar las credenciales",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        # limpiar la palabra "Bearer " si viaja en la cabecera
        if token.startswith("Bearer "):
            token = token.replace("Bearer ", "")

        payload = jwt.decode(token, key=SECRET_KEY, algorithms=[ALGORITHM])

        email:str = payload.get("email")
        name: str = payload.get("name")
        surname:str = payload.get("surname")
        rol:str = payload.get("rol", "empleado")

        if email is None:
            raise credentials_exception
        
        return {
            "email": email,
            "name": name,
            "surname": surname,
            "rol": rol
        }
    except jwt.ExpiredSignatureError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="El token JWT ha expirado",
            headers={"WWW-Authenticate": "Bearer"},
        )
    except jwt.PyJWTError:
        raise credentials_exception