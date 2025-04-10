from fastapi import FastAPI
from src.api.routes import user_authentication
from db import Sessionlocal
import uvicorn


app = FastAPI(title="Apply Mate API", version="1.0")

app.include_router(user_authentication.router,prefix="/api/v1")

@app.get('/')
def welcome():
    return {
        "message":"Welcome"
    }


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)