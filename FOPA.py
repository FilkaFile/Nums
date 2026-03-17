from dataclasses import dataclass
import uvicorn
from fastapi import FastAPI, Path, Query
from fastapi.responses import PlainTextResponse, FileResponse
from fastapi.middleware.cors import CORSMiddleware

import json
app = FastAPI()

My_Number = 1*3442


origins = ["*"]
app.add_middleware(CORSMiddleware, allow_origins=origins,
                   allow_methods=['*'], allow_headers=['*'])


my_us = {'1': 'Ivan', "2": 'Pavel', '3': 'Stepa'}

# 1


@app.get("/calc")
def get_calc(a: float, b: float, oper):
    if oper == 'add':
        res = a+b

    elif oper == 'subtract':
        res = a-b

    elif oper == 'multiply':
        res = a*b

    elif oper == 'divide':
        res = a/b

    else:
        res = 'null, одна ошибка и вы ошиблись'

    return {"результате": res}


# 2

bookshelf = list()
filtred_bookshelf = list()


@dataclass
class Book:
    id: int
    title: str
    author: str
    year: int
    genre: str


bookshelf = [
    Book(id=1, title='Война и пирог', author='Сергей', year=1990, genre='хоррор'),
    Book(id=2, title='Мэрри момент', author='Олег', year=2000, genre='хоррор'),
    Book(id=3, title='Потапыч', author='Олег', year=1890, genre='комедия'),
    Book(id=4, title='Мёртвые туши', author='Сергей', year=2000, genre='комедия'),
    Book(id=5, title='Шерлок Шомс', author='Сергей', year=2020, genre='комедия'),
    Book(id=6, title='Чипсик', author='Олег', year=2000, genre='комедия')
]


@app.get("/books")
def get_book(author: str = Query(default=''), genre: str = Query(default=''), min_year: int = Query(default=0), max_year: int = Query(default=0)):

    filtered_books = [book for book in bookshelf if (
        (not author or book.author == author) and
        (not genre or book.genre == genre) and
        (not min_year or book.year >= min_year) and
        (not max_year or book.year <= max_year)
    )]

    return save_to_json(filtered_books, 'filtered_books.json')


def save_to_json(filtered_books, filename):
    data = str(filtered_books)

    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

        return FileResponse("filtered_books.json", filename='filtered_books.json', media_type="application/octet-stream")

# 3


@dataclass
class Movie:
    id: int
    title: str
    views_history: list[int]


movies = [Movie(1, 'Абоба', [12, 123, 12, 54, 34, -65]),
          Movie(2, 'Фнаф', [110, -22, -32]),
          Movie(3, 'КрикАААА', [12, 123, 12, 54, 34, 65])
          ]


@app.get("/movies")
def get_movie(status: str | None = None, min_avg_views: int = Query(default=0)):
    filtr_movies = []
    for opa in movies:
        last_day = opa.views_history[-1]
        avg = sum(opa.views_history) / len(opa.views_history)
        rost = (last_day - avg) / avg * 100

        if rost > 20:
            trend_status = "Viral"

        elif -10 < rost <= 20:
            trend_status = "Stable"

        else:
            trend_status = "Fading"

        if trend_status == status and avg >= min_avg_views:
            filtr_movies.append(opa)

    return str(filtr_movies)


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


'''
@app.get('/', response_class=PlainTextResponse)
def read_root():
    data = "ОПАНА"
    return data

    html_content = '<h2>Hello world</h2>'
    return {"message": html_content}

'''


@app.get('/about')
def about():
    return {"message": "1 на сайте"}


if __name__ == "__main__":
    uvicorn.run('FAPI:app', host='0.0.0.0', port=8000, reload=True)
