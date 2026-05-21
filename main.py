# Habilitar CORS (Cross-Origin Resource Sharing) 

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from modules.auth import auth_controller
from modules.tasks import task_controller
from modules.events import event_controller
from modules.manuals import manual_controller

# python -m uvicorn main:app --reload para lanzar el servidor

app = FastAPI(
    title="API Rest con Angular y MongoDB",
    version="1.0.0"
    )

origins = [
   "http://localhost:4200", # servidor local de Angular
]

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = ["*"],  # Permite todos los metodos y encabezados.
    allow_headers = ["*"],
)

# Registrar controladores
app.include_router(auth_controller.router)
app.include_router(task_controller.router)
app.include_router(event_controller.router)
app.include_router(manual_controller.router)



@app.get("/")
def root():
    return {
        "status": "API Funcional",
        "message": "Listo para ser consumido por Angular"
    }