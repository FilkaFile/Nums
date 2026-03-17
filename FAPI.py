from dataclasses import dataclass
import uvicorn
from fastapi import FastAPI, Body, Path
from fastapi.responses import (
    Response, HTMLResponse, JSONResponse, PlainTextResponse, FileResponse, RedirectResponse)
from pydantic import BaseModel, Field


app = FastAPI()


class Person(BaseModel):
    name: str = Field(default='', min_length=0, max_length=50)
    age: int | None = None


@app.get("/")
def root():
    return FileResponse('public/index2.html')


@app.post("/hello")
def hello(person: Person):
    if person.age == None:
        return {"message": f"Привет {person.name}"}
    else:
        return {"message": f"Привет {person.name}, ваш возраст - {person.age}"}


@app.get('/', response_class=PlainTextResponse)
def read_root():
    data = "ОПАНА"
    return data


if __name__ == "__main__":
    uvicorn.run('FAPI:app', host='0.0.0.0', port=8000, reload=True)
