from fastapi import FastAPI, Depends
from models import Product
from database import session,engine
import database_models
from sqlalchemy.orm import Session
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(title=os.getenv("APP_NAME"), version=os.getenv("VERSION"), debug=os.getenv("DEBUG")=="True")
database_models.Base.metadata.create_all(bind=engine)

@app.get("/")
def greet():
    return "Hello, world!"

products =[
    Product(id=1,name="Phone",description="",price=20000,quantity=2),
    Product(id=2,name="Laptop",description="",price=200000,quantity=5)
]

def init_db():
    count = session().query(database_models.Product).count()
    if count == 0:
        db = session()
        for product in products:
            db_product = database_models.Product(**product.model_dump())
            db.add(db_product)
        db.commit()

init_db()

def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()

@app.get("/api/products",tags=["Product"])
def getProducts():
    return products

@app.post("/api/product",tags=["Product"])
def createProduct(product: Product):
    products.append(product)
    return product

@app.get("/api/product/{id}",tags=["Product"])
def getProduct(id: int):
    for product in products:
        if product.id == id:
            return product
    return {"message": "Product not found"}

@app.put("/api/product/{id}",tags=["Product"])
def updateProduct(id: int, updatedProduct: Product):
    for index, product in enumerate(products):
        if product.id == id:
            products[index] = updatedProduct
            return updatedProduct
    return {"message": "Product not found"}

@app.delete("/api/product/{id}",tags=["Product"])
def deleteProduct(id: int):
    for index, product in enumerate(products):
        if product.id == id:
            deleted_product = products.pop(index)
            return deleted_product
    return {"message": "Product not found"}

@app.get("/api/v2/products",tags=["Product"])
def getProducts(db: Session = Depends(get_db)):
    db_products = db.query(database_models.Product).all()
    return db_products

@app.get("/api/v2/product/{id}",tags=["Product"])
def getProduct(id: int, db: Session = Depends(get_db)):
    db_product = db.query(database_models.Product).filter(database_models.Product.id == id).first()
    if db_product:
        return db_product
    return {"message": "Product not found"}

@app.post("/api/v2/product",tags=["Product"])
def createProduct(product:Product,db:Session = Depends(get_db)):
    db_product = database_models.Product(**product.model_dump())
    db.add(db_product)
    db.commit()
    return product

@app.put("/api/v2/product/{id}",tags=["Product"])
def updateProduct(id:int, product:Product, db:Session = Depends(get_db)):
    db_product = db.query(database_models.Product).filter(database_models.Product.id == id).first()
    if db_product:
        db_product.name = product.name
        db_product.description = product.description
        db_product.price = product.price
        db_product.quantity = product.quantity
        db.commit()
        return product
    return {"message":"Product not found"}

@app.delete("/api/v2/product/{id}",tags=["Product"])
def deleteProduct(id:int, db:Session = Depends(get_db)):
    db_product = db.query(database_models.Product).filter(database_models.Product.id == id).first()
    if db_product:
        db.delete(db_product)
        db.commit()
        return {"message":"Product deleted successfully"}
    return {"message":"Product not found"}