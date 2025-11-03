from fastapi import FastAPI
from app.core.config import APP_NAME, VERSION, DEBUG
from app.api.routes.product import router as product_router
from app.db.base import Base  # ensures models are imported
from app.db.session import engine, SessionLocal
from app.services.product import seed_defaults

app = FastAPI(title=APP_NAME, version=VERSION, debug=DEBUG)

# Routers
app.include_router(product_router)


@app.get("/")
def greet():
    return "Hello, world!"


@app.on_event("startup")
def on_startup():
    # Create tables
    Base.metadata.create_all(bind=engine)
    # Seed defaults if empty
    db = SessionLocal()
    try:
        seed_defaults(db)
    finally:
        db.close()
