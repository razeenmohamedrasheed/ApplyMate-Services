from db import engine,Base
from src.models.model import Recruiters




Base.metadata.create_all(bind=engine)