from mybd import *
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import DeclarativeBase, sessionmaker

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


@app.get("/")
def main():
    return FileResponse('public/client.html')


@app.get('/api/users')
def get_people(db: Session = Depends(get_db)):
    return db.query(Person).all()


@app.get('/api/users/{id}')
def get_person(id, db: Session = Depends(get_db)):
    person = db.query(Person).filter(Person.id == id).first()
    if person == None:
        return JSONResponse(status_code=404, content={"message": "ПОльзователь выпал в осадок"})
    return person


@app.delete("/api/users/{id}")
def delete_per(id, db: Session = Depends(get_db)):
    person = db.query(Person).filter(Person.id == id).first()
    if person == None:
        return JSONResponse(status_code=404, content={"message": "ПОльзователь выпал в осадок"})
    db.delete(person)
    db.commit()
    return person


@app.post("/api/users")
def create_per(data=Body(), db: Session = Depends(get_db)):
    person = Person(name=data['name'], age=data['age'])
    db.add(person)
    db.commit()
    db.refresh(person)
    return person


# @app.put("/api/users")
# def update_per(data=Body(), db: Session = Depends(get_db)):
    # person
    # db.add(person)
    # db.commit()
    # db.refresh(person)
    # return person


if __name__ == "__main__":
    uvicorn.run('request:app', host='0.0.0.0', port=8000, reload=True)
