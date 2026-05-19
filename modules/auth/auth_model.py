from passlib.context import CryptContext
from core.config import database

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
users_collection = database.get_collection("users")

class AuthModel:
    @staticmethod
    def veerify_password(plain_pass:str, hash_pass:str) -> bool:
        return pwd_context.verify(plain_pass, hash_pass)
    
    @staticmethod
    async def find_user_by_email(email:str) -> dict | None:
        user = await users_collection.find_one({"email":email})
        return user
    
    @staticmethod
    async def create_user(user_data:dict) -> dict:

        result = await users_collection.insert_one(user_data)
        new_user = await users_collection.find_one({"id": result.inserted_id})
        return new_user
    

    @staticmethod
    def get_password_hash(plain_pass:str) -> str:
        # Truncar a 72 bytes para cumplir con límite de bcrypt
        plain_pass = plain_pass[:72]
        return pwd_context.hash(plain_pass)