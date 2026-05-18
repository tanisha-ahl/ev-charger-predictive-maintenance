from fastapi import FastAPI
from api.routes import ingest

app = FastAPI()

app.include_router(ingest.router)