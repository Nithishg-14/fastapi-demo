import os
from dotenv import load_dotenv

load_dotenv()

APP_NAME = os.getenv("APP_NAME", "FastAPI Demo")
VERSION = os.getenv("VERSION", "0.1.0")
DEBUG = os.getenv("DEBUG", "False") == "True"
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:user@localhost:5429/test_db")
