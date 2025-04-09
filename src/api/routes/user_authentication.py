from fastapi import APIRouter
from fastapi import File, UploadFile, Form
from src.schemas.registration import Register
import json
import os


router = APIRouter(prefix="/auth")

UPLOAD_DIR = os.path.join("src", "files")

@router.post('/register')
async def candidate_registration(payload: str = Form(...),file: UploadFile = File(...)):
    try:
        data = Register(**json.loads(payload))
        file_location = os.path.join(UPLOAD_DIR, file.filename)

        with open(file_location, "wb") as f:
            f.write(await file.read())

        return {"message": "Registered successfully", "file_saved_at": file_location,"name":data.username}

    except Exception as  e:
        print(e)
   




@router.get('/login')
def login():
    return {
        "message":"Welcome to the regis"
    }


