import os
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import FileResponse
from typing import List
from core.security import get_current_user
from modules.manuals.manual_schema import ManualResponseSchema
from modules.manuals.manual_model import ManualModel

router = APIRouter(prefix="/manuals", tags=["Manuales Técnicos"])

@router.get("/", response_model=List[ManualResponseSchema])
async def read_manuals(current_user:dict = Depends(get_current_user)):
    return await ManualModel.get_all()


@router.get("/download/{file_name}")
async def download_manual(file_name:str, current_user:dict = Depends(get_current_user)):

    file_path= os.path.join("uploads", file_name)

    if not os.path.exists(file_path):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Documento no existe en servidor")
    
    return FileResponse(
        path=file_path,
        media_type="application/pdf",
        filename=file_name,
        status_code=status.HTTP_200_OK
    )