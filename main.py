from fastapi import FastAPI
from src.models import fastapi_models
from src.database_fastapi import engine
from src.routers import user_fastapi, auth_fastapi
from src.routers.residential import residential, userauth
from config import get_settings
import uvicorn

app = FastAPI()

fastapi_models.Base.metadata.create_all(engine)

app.include_router(auth_fastapi.router)
app.include_router(user_fastapi.router)
app.include_router(userauth.router)
app.include_router(residential.router)


if __name__ == '__main__':
    uvicorn.run(app, host=get_settings().uvicorn_host, port=get_settings().uvicorn_port)


