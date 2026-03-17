from dataclasses import dataclass
import uvicorn
from fastapi import FastAPI, Body, Path
from fastapi.responses import (
    Response, HTMLResponse, JSONResponse, PlainTextResponse, FileResponse, RedirectResponse)
from pydantic import BaseModel, Field


app = FastAPI()


class Person(BaseModel):
    name: str = Field(default='none', min_length=0, max_length=50)
    age: int | None = None


class Company(BaseModel):
    name: str


@app.get("/")
def root():
    return FileResponse('public/index2.html')


@app.post("/hello")
def hello(person: list[Person]):
    people = ""
    for p in person:
        people += str(p)
    return {"message": people}
    if person.age == None:
        return {"message": f"Привет {person.name}"}
    else:
        return {"message": f"Привет {person.name}, ваш возраст - {person.age}"}


@app.get('/')
def read_root():
    return FileResponse("public/index2.html")


if __name__ == "__main__":
    uvicorn.run('FAPI:app', host='0.0.0.0', port=8000, reload=True)
