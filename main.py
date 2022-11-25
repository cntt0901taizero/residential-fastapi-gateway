from fastapi import FastAPI
from src.models import fastapi_models
from src.database_fastapi import engine
from src.routers import user, authentication, residential
import uvicorn

app = FastAPI()

fastapi_models.Base.metadata.create_all(engine)

app.include_router(authentication.router)
app.include_router(user.router)
app.include_router(residential.router)


if __name__ == '__main__':
    uvicorn.run(app, host='localhost', port=8001)


