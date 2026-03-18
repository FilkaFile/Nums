from dataclasses import dataclass
import uvicorn
from fastapi import FastAPI, Body, Path, status, Form, Query, Cookie
from fastapi.responses import (
    Response, HTMLResponse, JSONResponse, PlainTextResponse, FileResponse, RedirectResponse)
from pydantic import BaseModel, Field
import uuid


app = FastAPI()


@app.get('/')
def root():
    return FileResponse('C:/Users/student/.vscode/new_proj2/public/index.html')


@app.post('/postdata')
def postdata(username=Form(), userage=Form()):
    return {"name": username, "age": userage}


if __name__ == "__main__":
    uvicorn.run('headers:app', host='0.0.0.0', port=8000, reload=True)
