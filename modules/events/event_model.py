from bson import ObjectId
from core.config import database

events_collection = database.get_collection("events")

class EventModel:

    @staticmethod
    def _map_event(event:dict) -> dict | None:
        if not event:
            return None
        return {
            "id": str(event["_id"]),
            "date": event.get("date", ""),
            "text": event.get("text", "")
        }
    
    @staticmethod
    async def get_all_by_user(email:str) -> list:
        events = []
        cur = events_collection.find({"user_email": email})
        async for doc in cur:
            mapped = EventModel._map_event(doc)
            if mapped:
                events.append(mapped)
        
        return events


    @staticmethod
    async def create(date:str, text:str, email:str) -> dict:
        new_event = {
            "date": date,
            "text": text,
            "user_email": email
        }

        result = await events_collection.insert_one(new_event)
        inserted = await events_collection.find_one({"_id": result.inserted_id})

        return EventModel._map_event(inserted)
    
    @staticmethod
    async def delete(event_id:str, email:str) -> bool:
        try:
            
            result = await events_collection.delete_one({
                "_id": ObjectId(event_id),
                "user_email": email
            })

            return result.deleted_count > 0
        except Exception as e:
            print(f"Error interno al borrar evento en MongoDB: {e}")
            return False