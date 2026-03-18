from SQLAlchemyy import *
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import DeclarativeBase, sessionmaker
from pydantic import BaseModel
from fastapi import FastAPI, Body, Path, status, Form, Query, Depends, Cookie, Body
from fastapi.responses import (
    Response, HTMLResponse, JSONResponse, PlainTextResponse, FileResponse, RedirectResponse)
import uvicorn

app = FastAPI()

Base.metadata.create_all(bind=engine)


class ProductCreate(BaseModel):
    id: int
    name: str
    price: float
    stock: int


def get_db():
    bd = SessionLocal()
    try:
        yield bd
    finally:
        bd.close()


@app.get("/")
def main():
    return FileResponse('public/client.html')


@app.get('/products/')
def get_prod(db: Session = Depends(get_db)):
    return db.query(Product).all()


@app.get('/stats/')
def get_stats(db: Session = Depends(get_db), data=Body()):
    total_inventory_value += data['price'] * data['stock']
    return {'total_inventory_value': total_inventory_value}


@app.post("/buy/{product_id}")
def buy_prod(product_id: int, db: Session = Depends(get_db), quantity: int = Query(default=1)):

    product = db.query(Product).filter(
        Product.id == product_id).first()

    if quantity <= 0:
        return JSONResponse(status_code=400, content={"message": "Ачо, нипон, а где количество товара?"})

    if product == None:
        return JSONResponse(status_code=404, content={"message": "А где, а нет такого товара"})

    if product.stock < quantity:
        return JSONResponse(status_code=400, content={"message": "А вот закончился товар"})

    product.stock -= quantity
    db.commit()
    db.refresh(product)

    return {'message': 'Покупка прошла успешно! Вы теперь банкрот)'}


@app.post("/products/")
def create_prod(db: Session = Depends(get_db), data=Body(), quantity: int = Query(default=1)):

    product = db.query(Product).filter(Product.name == data['name']).first()

    if product:
        product.stock += quantity
        product.price = data['price']

        db.add(product)
        db.commit()

    product = Product(name=data['name'],
                      price=data['price'], stock=data['stock'])

    db.add(product)
    db.commit()
    db.refresh(product)
    return {"id": product.id, "name": product.name, "price": product.price, "stock": product.stock}


if __name__ == "__main__":
    uvicorn.run('server:app', host='0.0.0.0', port=8000, reload=True)
