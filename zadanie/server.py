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


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/", summary='Открываем HTML-ку', description='Функция для открытия нашего html-а')
def main():
    return FileResponse('public/client.html')


@app.get('/products/', summary="Получить все добавленные продукты", description='Функция для получения всех продуктов из JSON-а:')
def get_prod(db: Session = Depends(get_db)) -> str:
    return db.query(Product).all()


@app.get('/stats/', summary='Получить общую стоимость склада', description="Функция для получения общей стоимости склада:")
def get_stats(db: Session = Depends(get_db)) -> str:
    total_inventory_value = 0
    products = db.query(Product).all()
    for p in products:
        total_inventory_value += p.price * p.stock
    return {'total_inventory_value': total_inventory_value}


@app.post("/buy/{product_id}", summary='Купить товар', description='Функция для покупоЧЕК товаров:')
def buy_prod(product_id: int = Path(description='Id продукта'), db: Session = Depends(get_db), quantity: int = Query(default=1, description='Кол-во товара для покупки')) -> str:

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


@app.post("/products/", summary='Добавить продукты', description='Функция для добавления/обновления продукта')
def create_prod(db: Session = Depends(get_db), data: ProductCreate = Body(description="добавляем/обновляем продукт")) -> str:

    product = db.query(Product).filter(Product.name == data.name).first()

    if product:
        product.stock += data.stock
        product.price = data.price

        db.add(product)
        db.commit()
        db.refresh(product)

    else:
        product = Product(name=data.name,
                          price=data.price, stock=data.stock)

        db.add(product)
        db.commit()
        db.refresh(product)

    return {"id": product.id, "name": product.name, "price": product.price, "stock": product.stock}


if __name__ == "__main__":
    uvicorn.run('server:app', host='0.0.0.0', port=8000, reload=True)
