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