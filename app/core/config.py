import os

class Settings:
    PROJECT_NAME = "Financial Document API"
    VERSION = "1.0.0"

settings = Settings()

SECRET_KEY = "your_secret_key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60