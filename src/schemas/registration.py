from pydantic import BaseModel

class Register(BaseModel):
    username : str
    email : str
    dob : str
    gender : str
    contact : str
    github : str
    linkedin:str
    password : str
    experienced: bool
