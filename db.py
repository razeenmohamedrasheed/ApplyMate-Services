from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Replace with your DB credentials
DATABASE_URL = "postgresql://postgres:Admin@localhost/applymate"
# DATABASE_URL = "mysql+pymysql://user:password@localhost/dbname"
engine=create_engine(DATABASE_URL,echo=True)
Base=declarative_base()

Sessionlocal=sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = Sessionlocal()
    try:
        yield db
    finally:
        db.close()