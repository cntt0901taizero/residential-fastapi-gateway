import logging
from pathlib import Path

import uvicorn
from fastapi import FastAPI

from app.exceptions.exception_handlers import add_exception_handlers
from app.routers import userauth, residential
from configs import get_settings

app = FastAPI()
app.include_router(userauth.router)
app.include_router(residential.router)

BASE_DIR: str = str(Path(__file__).resolve().parent.parent)


@app.on_event("startup")
async def startup_event():
    logger = logging.getLogger("uvicorn.access")
    handler = logging.FileHandler(f'{BASE_DIR}/logs/logs_file.log', mode='w')
    handler.setFormatter(logging.Formatter("%(asctime)s %(levelname)s [ in %(pathname)s:%(lineno)d] %(message)s"))
    logger.addHandler(handler)


add_exception_handlers(app)

if __name__ == '__main__':
    uvicorn.run(app, host=get_settings().uvicorn_host, port=int(get_settings().uvicorn_port))
