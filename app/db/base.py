from sqlalchemy.orm import declarative_base

Base = declarative_base()
 
# Import models here so metadata includes all tables when creating
# Avoid unused import warnings with noqa comment
from app import models  # noqa: F401
from app.models import product  # noqa: F401
