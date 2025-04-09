from pydantic import BaseModel

class Register(BaseModel):
    username : str
    email : str
    dob : str
    gender : str
    resume : str
    contact : str
    linkedin:str
    password : str
    experienced: bool
    role_id : int 