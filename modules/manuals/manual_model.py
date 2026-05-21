from core.config import database

manuals_collection = database.get_collection("manuals")

class ManualModel:

    @staticmethod
    def _map_manual(manual:dict) -> dict | None:
        if not manual:
            return None
        
        file_name = manual.get("file_name", "documento_no_disponible.pdf")

        return {
            "id": str(manual["_id"]),
            "code": manual.get("code", ""),
            "title": manual.get("title", ""),
            "version": manual.get("version", ""),
            "departament": manual.get("departament", ""),
            "pdf_url": f"http://localhost:8000/manuals/download/{file_name}"
        }
    
    @staticmethod
    async def get_all() -> list:
        manuals = []
        cur= manuals_collection.find()
        async for doc in cur:
            mapped = ManualModel._map_manual(doc)
            if mapped:
                manuals.append(mapped)
        
        return manuals