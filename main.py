from fastapi import FastAPI
from src.models import fastapi_models
from src.database_fastapi import engine
from src.routers import user_fastapi, auth_fastapi, residential
import uvicorn

app = FastAPI()

fastapi_models.Base.metadata.create_all(engine)

app.include_router(auth_fastapi.router)
app.include_router(user_fastapi.router)
app.include_router(residential.router)


if __name__ == '__main__':
    uvicorn.run(app, host='10.32.47.64', port=8000)
    # uvicorn.run(app, host='localhost', port=8000)


