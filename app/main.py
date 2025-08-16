from fastapi import FastAPI
from app.routes import properties, reservations

app = FastAPI(title="Seazone API")

app.include_router(reservations.router)
app.include_router(properties.router)