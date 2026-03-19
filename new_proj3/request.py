
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import DeclarativeBase, sessionmaker

from fastapi import FastAPI, Body, Path, status, Form, Query, Depends, Cookie, Body
from fastapi.responses import (
    Response, HTMLResponse, JSONResponse, PlainTextResponse, FileResponse, RedirectResponse)
import uvicorn
import database
import models
import shemas

app = FastAPI()
database.Base.metadata.create_all(bind=database.engine)


def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def main():
    return FileResponse('public/client1.html')


@app.get('/api/users')
def get_people(db: Session = Depends(get_db)):
    return db.query(models.Person).all()


@app.get('/api/users/{id}', response_model=shemas.PersonResponce)
def get_person(id, db: Session = Depends(get_db)):
    person = db.query(models.Person).filter(models.Person.id == id).first()
    if person == None:
        return JSONResponse(status_code=404, content={"message": "ПОльзователь выпал в осадок"})
    return person


@app.delete("/api/users/{id}", response_model=shemas.PersonResponce)
def delete_per(id, db: Session = Depends(get_db)):
    person = db.query(models.Person).filter(models.Person.id == id).first()
    if person == None:
        return JSONResponse(status_code=404, content={"message": "ПОльзователь выпал в осадок"})
    db.delete(person)
    db.commit()
    return person


@app.post("/api/users", response_model=shemas.PersonCreate)
def create_per(data: shemas.PersonCreate = Body(), db: Session = Depends(get_db)):
    person = models.Person(name=data['name'], age=data['age'])
    db.add(person)
    db.commit()
    db.refresh(person)
    return person


@app.post("/api/companies", response_model=shemas.CompanyResponse)
def create_company(company: shemas.CompanyCreate, db: Session = Depends(get_db)):
    db_company = models.Company(name=company.name)
    db.add(db_company)
    db.commit()
    db.refresh(db_company)
    return db_company


if __name__ == "__main__":
    uvicorn.run('request:app', host='0.0.0.0', port=8000, reload=True)
