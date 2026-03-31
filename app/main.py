from fastapi import FastAPI
from app.api import auth, users
from app.Database.db import engine
from app.Database.models import Base

Base.metadata.create_all(bind=engine)

app = FastAPI()

# Include routes
app.include_router(auth.router)
app.include_router(users.router)

@app.get("/")
def home():
    return {"message": "API is running"}