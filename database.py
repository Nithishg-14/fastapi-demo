from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

db_url = "postgresql://postgres:user@localhost:5429/test_db"
engine = create_engine(db_url)
session = sessionmaker(autocommit=False,autoflush=False,bind=engine)