from dataclasses import dataclass
import uvicorn
from fastapi import FastAPI, Body, Path, status
from fastapi.responses import (
    Response, HTMLResponse, JSONResponse, PlainTextResponse, FileResponse, RedirectResponse)
from pydantic import BaseModel, Field
import uuid


app = FastAPI()


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.id = str(uuid.uuid4)


people = [Person('Том', 38),
          Person('Женя', 50),
          Person('Томям', 34)]


def find_person(id):
    for person in people:
        if person.id == id:
            return person
    return None


@app.get('/api/users')
def get_people():
    return people


@app.get('/')
def root():
    return FileResponse("public/index.html")


@app.get("/api/users/{id}")
def get_perdon(id):
    person = find_person(id)
    if person == None:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={"message": "Пользователь хз где"}
        )
    return person


@app.delete("/api/users/{id}")
def delete_perdon(id):
    person = find_person(id)
    if person == None:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={"message": "Пользователь хз где"}
        )
    people.remove(person)
    return person


@app.post("/api/users")
def create_person(data=Body()):
    person = Person(data["name"], data["age"])
    people.append(person)
    return person


@app.put("/api/users/{id}")
def edit_peron(data=Body()):
    person = find_person(data["id"])
    if person == None:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={"message": "Пользователь хз где"}
        )
    person.age = data["age"]
    person.name = data["name"]

    return person


if __name__ == "__main__":
    uvicorn.run('main:app', host='0.0.0.0', port=8000, reload=True)
