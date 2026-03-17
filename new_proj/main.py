from dataclasses import dataclass
import uvicorn
from fastapi import FastAPI, Body, Path
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


if __name__ == "__main__":
    uvicorn.run('main:app', host='0.0.0.0', port=8000, reload=True)
