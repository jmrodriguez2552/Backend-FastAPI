from bson import ObjectId
from core.config import database

task_collection = database.get_collection("tasks")

class TaskModel:

    @staticmethod
    def _map_task(task:dict) -> dict | None:
        # Transformar el _id de MongoDB a un string id legible
        if not task:
            return None
        return {
            "id": str(task["_id"]),
            "title": task.get("title", ""),
            "completed": task.get("completed", False)
        }
    
    @staticmethod
    async def get_all_by_user(email:str):
        tasks = []
        cur = task_collection.find({"user_email": email})
        async for task in cur:
            mapped = TaskModel._map_task(task)
            if mapped:
                tasks.append(mapped)
        
        return tasks


    @staticmethod
    async def create(title:str, email:str) -> dict:
        new_task_dict = {
            "title": title,
            "completed" : False,
            "user_email": email
        }
    
        result = await task_collection.insert_one(new_task_dict)
        inserted_task = await task_collection.find_one({"_id": result.inserted_id})
        return TaskModel._map_task(inserted_task)
    

    @staticmethod
    async def update_status(task_id:str, completed:bool, email:str) -> dict| None:

        from pymongo import ReturnDocument

        result = await task_collection.find_one_and_update(
            {
                "_id": ObjectId(task_id),
                "user_email": email
            },
            {
                "$set": {"completed" : completed}
            },
            return_document=ReturnDocument.AFTER
        )
        return TaskModel._map_task(result) if result else None
    

    @staticmethod
    async def delete(task_id:str, email:str) -> bool:
        result = await task_collection.delete_one({"_id": ObjectId(task_id), "user_email": email})
        return result.deleted_count > 0