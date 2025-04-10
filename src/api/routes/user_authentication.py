from fastapi import APIRouter, Depends, HTTPException
from fastapi import File, UploadFile, Form
from src.schemas.registration import Register
from src.utils.password_utils import Hash
from sqlalchemy.orm import Session
from src.models.model import Candidates
from db import get_db
import json
import os


router = APIRouter(prefix="/auth")

UPLOAD_DIR = os.path.join("src", "files")

@router.post('/register')
async def candidate_registration(payload: str = Form(...),file: UploadFile = File(...), db: Session = Depends(get_db)):
    try:
        data_dict = json.loads(payload)
        data = Register(**data_dict)

        existing_user = db.query(Candidates).filter(Candidates.email == data.email).first()
        if existing_user:
            raise HTTPException(status_code=400, detail="User already exists")
        

        encrypt_password = Hash.get_password_hash(data.password)

        file_location = os.path.join(UPLOAD_DIR, file.filename)
        with open(file_location, "wb") as f:
            f.write(await file.read())
        print(file.filename)
       
        new_user = Candidates(
            role_id = 3,
            username=data.username,
            email=data.email,
            contact=data.contact,
            dob=data.dob,
            gender = data.gender,
            github_url = data.github,
            linkedin_url = data.linkedin,
            resume = file.filename,
            has_experience = data.experienced,
            password= encrypt_password
        )
        print(new_user)
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
     
        return {"message": "Registered successfully"}

    except Exception as  e:
        print(e)
   




@router.get('/login')
def login():
    return {
        "message":"Welcome to the regis"
    }


