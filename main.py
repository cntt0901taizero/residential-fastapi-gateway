import logging

import uvicorn
from fastapi import FastAPI

from config import get_settings
from src.routers.residential import residential, userauth

app = FastAPI()
app.include_router(userauth.router)
app.include_router(residential.router)


@app.on_event("startup")
async def startup_event():
    logger = logging.getLogger("uvicorn.access")
    handler = logging.FileHandler('logs_file.log', mode='w')
    # handler.setLevel(level=logging.INFO)
    handler.setFormatter(logging.Formatter("%(asctime)s %(levelname)s [ in %(pathname)s:%(lineno)d] %(message)s"))
    logger.addHandler(handler)



if __name__ == '__main__':
    uvicorn.run(app, host=get_settings().uvicorn_host, port=get_settings().uvicorn_port)





