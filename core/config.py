import os
from motor.motor_asyncio import AsyncIOMotorClient

# Configuración BD Mongo
MONGO_DETAILS = "mongodb://127.0.0.1:27017/?directConnection=true"  # Cambia por tu URI de Atlas si usas la nube
SECRET_KEY = "52414589G"  
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

client = AsyncIOMotorClient(MONGO_DETAILS)

database = client.employees