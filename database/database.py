from sqlalchemy import create_engine
# from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, declarative_base  # NEWWWW

# DATABASE_URL = "mysql+mysqlconnector://sail:password@localhost:3306/testing"
# DATABASE_URL = "mysql+mysqlconnector://root@localhost:3306/fastapi_task"
DATABASE_URL = "mysql+mysqlconnector://root@localhost:3306/fastapi_task_testing"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base() # NEWWWW

def get_database_session():
    try:
        db = SessionLocal()
        yield db
        #return db
    finally:
        db.close()