from fastapi import FastAPI
from models import Product

app = FastAPI()

@app.get("/")
def greet():
    return "Hello, world!"

products =[
    Product(id=1,name="Phone",description="",price=20000,quantity=2),
    Product(id=2,name="Laptop",description="",price=200000,quantity=5)
]

@app.get("/api/products",tags=["User"])
def getProducts():
    return products

@app.post("/api/products",tags=["User"])
def createProduct():
    return products