import uvicorn
from fastapi import FastAPI
from fastapi.responses import HTMLResponse, JSONResponse, Response, PlainTextResponse, FileResponse
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

My_Number = 1*3442


origins = ["*"]
app.add_middleware(CORSMiddleware, allow_origins=origins,
                   allow_methods=['*'], allow_headers=['*'])


my_us = {'1': 'Ivan', "2": 'Pavel', '3': 'Stepa'}


@app.get('/users/{id}/{age}')  # Шаблон
def get_users(id, age):
    return str(my_us.get(id)) + " age " + str(age)


@app.get('/num')
def mynum():
    return My_Number


@app.get('/foo')
def root_file():
    return FileResponse("public/ooo.docx", filename='ooo.docx', media_type="application/octet-stream")


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
