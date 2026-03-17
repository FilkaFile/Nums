from dataclasses import dataclass
import uvicorn
from fastapi import FastAPI, Body, Path, status, Query
from fastapi.responses import (
    Response, HTMLResponse, JSONResponse, PlainTextResponse, FileResponse, RedirectResponse)
from pydantic import BaseModel, Field
import uuid


app = FastAPI()


class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.id = str(uuid.uuid4())


items_db = [Item('Молоко', 38),
            Item('Хлеб', 50),
            Item('Масло', 34)]


@app.post("/items", summary="Создать предмет", description="Добавляет предмет с указанной ценой и именем")
def create_item(data=Body()):
    item = Item(data["name"], data["price"])
    items_db.append(item)
    return items_db


@app.get('/items', summary="Получить список всех предметов", description="Возвращает все предметы какие есть")
def get_item():
    return items_db


@app.get("/", summary="Индекс", description="Через него мы открываем наш .html файл")
def index():
    return FileResponse("public/index.html")


def find_item(id):
    for item in items_db:
        print(item.id, id)
        if str(item.id) == str(id):
            return item
    return None


@app.get("/items/{id}", summary="Получить предмет", description='Получает предмет по указанному id')
def get_item(id):
    item = find_item(id)
    if item == None:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={"message": "Товар хз где"}
        )
    return item


@app.delete("/items/{id}", summary="Удалить предмет", description="Удалает предмет по id")
def delete_item(id):
    item = find_item(id)
    if item == None:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={"message": "Товар хз где"}
        )
    items_db.remove(item)

    return JSONResponse(
        content={"message": "Удалено"}
    ), item


@app.put("/items/{id}", summary='Изменить предмет', description="Изменяет название и цену предмета на указанные, тоже по id")
def edit_item(id, data=Body()):
    item = find_item(id)
    if item == None:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={"message": "Товар хз где"}
        )

    item.price = data["price"]
    item.name = data["name"]

    return item


if __name__ == "__main__":
    uvicorn.run('main:app', host='0.0.0.0', port=8000, reload=True)
