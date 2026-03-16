import uvicorn
from fastapi import FastAPI, Path, Query
from fastapi.responses import HTMLResponse, JSONResponse, Response, PlainTextResponse, FileResponse
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

My_Number = 1*3442


origins = ["*"]
app.add_middleware(CORSMiddleware, allow_origins=origins,
                   allow_methods=['*'], allow_headers=['*'])


my_us = {'1': 'Ivan', "2": 'Pavel', '3': 'Stepa'}


@app.get("/cats")
def get_cat(name: list[str] = Query(default='whdd', min_length=3, max_length=10)):
    return {"cat_name": name}


@app.get("/users/admin")
def admin():
    return {"mess": "пупупуууу"}


@app.get('/users/{name}')
def users(name: str = Path(min_length=1, max_length=10), age: int = Query(ge=18, lt=101)):
    return {'users': name, "age": age}


@app.get('/users/{id}/{age}')  # Шаблон
def get_users(id: int, age: int):
    return str(my_us.get(id)) + " age " + str(age)


@app.get('/num')
def mynum():
    return My_Number


@app.get('/foo')
def root_file():
    return FileResponse("FAPI.py", filename='FAPI.py', media_type="application/octet-stream")


@app.get('/', response_class=PlainTextResponse)
def read_root():
    data = "ОПАНА"
    return data

    html_content = '<h2>Hello world</h2>'
    return {"message": html_content}


@app.get('/about')
def about():
    return {"message": "1 на сайте"}


if __name__ == "__main__":
    uvicorn.run('FAPI:app', host='0.0.0.0', port=8000, reload=True)
