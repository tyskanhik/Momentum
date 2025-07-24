from dotenv import load_dotenv
import os

load_dotenv()

class Config:
    ALLOWED_ORIGINS = ["http://localhost:4200"]
    STATIC_DIR = "app/static"