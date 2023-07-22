import asyncio

import httpx
import pytest
from api import app

@pytest.fixture(scope="session")
def event_loop():
    # loop = asyncio.get_running_loop()
    loop = asyncio.new_event_loop()
    print("aaaaaaa")
    print(loop)
    yield loop
    loop.close()


# async def init_db():
#     # test_settings = Settings()
#     # test_settings.DATABASE_URL = "mongodb://localhost:27017/testdb"

#     # await test_settings.initialize_database()
#     # DATABASE_URL = "mysql+mysqlconnector://root@localhost:3306/fastapi_task_testing"

#     engine = create_engine(database.DATABASE_URL)
#     SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

#     Base = declarative_base()
#     Base.metadata.create_all(bind=engine)

#     db = SessionLocal()
#     return db

@pytest.fixture(scope="session")
async def default_client():
    async with httpx.AsyncClient(app=app, base_url="http://app") as client:
        yield client
        # db.query(models.Category).delete()
        # db.query(models.Task).delete()
        # db.query(models.User).delete()
