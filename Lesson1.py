# HFEGebf

from datetime import datetime, timedelta
import datetime
import time
import math
from math import sqrt, pi
import json
from datetime import datetime


class DataBase:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self, user, psw, port):
        self.user = user
        self.psw = psw
        self.port = port

    def connect(self):
        print(f"Соединение с БД: {self.user}, {self.psw}, {self.port}")

    def close(self):
        print("Закрытие соединения")
        return "Данные из БД"

    def write(self):
        print(f"Запись в БД: {self.user}, {self.psw}, {self.port}")


class ExceptionPrintSendData(Exception):
    def __init__(self, *args):
        self.message = args[0] if args else None

    def __str__(self):
        return ('Ошибка')


class PrintData:

    def print(self, data):
        self.send_data(data)
        print(f'Печать {str(data)}')

    def send_data(self, data):
        if not self.send_to_print(data):
            raise Exception('Принтер усо')

    def send_to_printer(self, data):
        return False

# 1


class Employee:
    company = 'A'

    def __init__(self, n, s):
        self.name = n
        self.salary = s

    def get_info(self):
        return print(f'Имя: {self.name}, зарплата: {self.salary}, компания: {self.company}')


# a = Employee('Anna', 12212)
# a.get_info()

# 2


class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def set_coords(self, x, y):
        if (isinstance(x, (int, float)) and isinstance(y, (int, float))) or (str(x).isdigit() and str(y).isdigit()):
            self.x = x
            self.y = y
        else:
            raise ValueError

    def get_coords(self):
        return (self.x, self.y)


# a = Point()
# a.set_coords(1.4, 1.4)
# a.get_coords()

# 3


class Product:
    name = ''
    sale = 0
    num = 0

    def __init__(self, name, sale, num):
        self.name = name
        self.sale = sale
        self.num = num


class ShoppingCart:
    def __init__(self):
        self.products = {}
        self.total_sale = 0

    def add_product(self, product_name, num_to_buy):
        self.products[product_name.name] = {
            'product_name': product_name, 'num': num_to_buy}
        self.total_sale += product_name.sale * num_to_buy
        print(
            f'Добвален продукт {product_name.name}, ценой {self.total_sale}, в кол-ве {num_to_buy}')

    def remove_product(self, name, num, product):
        self.names.remove(name)
        self.nums -= num
        self.sales -= Product.sale

    def get_total(self):
        print(self.sales)


# a = Product('banana', 10, 5)

# b = ShoppingCart()
# b.add_product('banana', 2)

class Vector:
    MIN_COORD = 0
    MAX_COORD = 100

    def __init__(self, x, y):
        self.x = self.y = 0
        if self.validate(x) and self.validate(y):
            self.y = y
            self.x = x
            print(self.norm2(x, y))

    def get_coord(self):
        return self.x, self.y

    @classmethod
    def validate(cls, arg):
        return cls.MIN_COORD <= arg <= cls.MAX_COORD

    @staticmethod
    def norm2(x, y):
        return x*x + y*y


'''
v = Vector(10, 20)
coord2 = Vector.get_coord(v)
res = Vector.validate(5)
res2 = Vector.norm2(23, 32)
print(res, res2)
'''

'''
class Point:
    MAX_COORD = 100
    MIN_COORD = 0

    def __init__(self, x=0, y=0, z=0):
        self.__x = self.__y = 0
        if self.__check_value(x) and self.__check_value(y) and self.__check_value(z):
            self.__x = x
            self.__y = y
            self.__z = z

    def set_coord(self, x, y, z):
        if self.MIN_COORD <= x <= self.MAX_COORD:
            if type(x) in (int, float) and type(y) in (int, float) and type(z) in (int, float):
                self.__x = x
                self.__y = y
                self.__z = z

    def __getattribute__(self, item):
        if item == "_Point__x":
            raise ValueError("PrivateError")
        else:
            return object.__getattribute__(self, item)

    def __setattr__(self, key, value):
        if key == "z":
            raise AttributeError('Низя такое имя')
        else:
            # self.__dict__[key] = value
            # self.__x = value
            object.__setattr__(self, key, value)

    def __getattr__(self, item):
        return False

    def __delattr__(self, item):
        print("__dellattr__" + item)
        object.__delattr__

    def get_coord(self):
        return print(self.__x, self.__y, self.__z)

    @classmethod
    def set_bound(cls, left):
        cls.MIN_COORD = left

    @classmethod
    def __check_value(cls, x):
        return type(x) in (int, float)


pt = Point(1, 2, 3)
pt.set_coord(5, 6, 7)
pt.get_coord()

pt.set_bound(10)
pt.set_coord(2, 2, 3)
pt.get_coord()

pt.a = 10
del pt.a
print(pt.__dict__)
'''

# 10 классов/функций для вашего сайта
# Регистрация на сайте онлайн игры??
'''

class ACCOUNT:
    reg = {}

    def create_acc(self, login, password):  # Создание акка
        if login not in self.reg:

            self.reg[login] = password

            print(f'Успешно создан аккаунт {login}')
        else:
            print(f'Пользователь с логином {login} уже существует!')

    def rename_acc(self, old_login, new_login):  # Пермеинование акка
        if new_login != old_login and new_login not in self.reg:
            password = self.reg[old_login]
            del self.reg[old_login]
            self.reg[new_login] = password
            print(f'Аккаунт {old_login} успешно переименован в {new_login}')
        else:
            print(f'Пользователь с логином {old_login} уже существует!')

    def enter_in_acc(self, login, password):  # Вход в акк
        if login not in self.reg:
            print('Отказано в доступе! Неверный логин')
        else:
            check_password = self.reg[login]
            if password == check_password:
                print(f'Подтверждение входа пользователя {login}')
            else:
                print('Отказано в доступе! Неверный пароль.')

    def get_logs(self):  # Отправляем лог сайту
        print("Зарегистрированные логины и их пароли:")
        return print(self.reg)


class GAME:
    login = 'null'
    records = ''
    money = ''

    game_progress = {}

    # Запись очков и игровой валюты на счету пользователя
    def win_the_match(self, login, records, money):
        if login not in ACCOUNT.reg:
            print('Пользователь не найден')
        else:
            self.game_progress = {login: [records, money]}

    def check_records(self, login):  # проверить очки и игровой валюты на счету пользователя
        if login not in ACCOUNT.reg:
            print('Пользователь не найден')
        else:
            return print(self.game_progress[login])


a = ACCOUNT()

print('Ведите номер требуемой команды:')
print('1: Создать аккаунт')
print('2: Войти в аккаунт')
print('3: Переименовать аккаунт')
print('4: Получить Логи (пароли и логины всех аккаунтов)')
print('exit: Выйти')

chose = input()

while chose != 'exit':

    if chose == '1':
        a.create_acc(input(), int(input()))
        print(a.reg)

    if chose == '2':
        a.enter_in_acc(input(), int(input()))
        pass

    if chose == '3':
        a.rename_acc(input(), input())
        pass

    if chose == '4':
        a.get_logs()
        pass

    chose = input()


b = GAME()
b.win_the_match('Open31', 100, 121)
b.check_records('Open31')
'''

'''
data = {"username": "Ivan",
        "created_at": datetime.now().isoformat()}

json.dumps(data)

data2 = ["python", "api", "json"]
json.dumps(data2)


class DB_CONN:
    def __init__(self):
        pass


class User:
    def __init__(self, username, password):
        self.username = username
        self.__password = self.__hash__()
        self.__db_session = DB_CONN()
        self.created_at = datetime.now()

    def _to_dict(self):
        return {"username": self.username,
                "created_at": self.created_at.isoformat()}


user = {
    "id": 1,
    "username": "Ivan",
    "email": "ivan@ava.com",
    "profile": {
        "level": 15,
        "experience": 7500,
        "rank": "Gold",
        "avatar": "url"
    },
    "inventory": [
        {"item": "sword", "quantity": 1},
        {"item": "potion", "quantity": 5}
    ]
}

print(user)

user = User("Ivan", "secret")
print(user.__dict__)
json.dumps(user._to_dict())

with open("user_data.json", "w", encoding="utf-8") as json_file:
    json.dump(user._to_dict(), json_file)

with open("user_data.json", encoding="utf-8") as reading_file:
    json.dump(user._to_dict(), json_file)

# user["inventory"] = user
# json.dumps(user._to_dict())
'''

'''
class Person:
    S_RUS = 'абвгдеёжзийклмнопрстъьэюя'
    S_RUS_UPPER = S_RUS.upper()

    def __init__(self, fio, name, old, ps, weight):
        self.verify_fio(fio)

        self.fio = fio.split()

        self.__name = name
        self.__old = old
        self.__ps = ps
        self.weight = weight

    @classmethod
    def verify_fio(cls, fio):
        if type(fio) != str:
            raise TypeError('ФИО НЕ СТРОКА')
        f = fio.split()
        if len(f) != 3:
            raise TypeError("Формат неверный")
        letters = cls.S_RUS + cls.S_RUS_UPPER
        for s in f:
            if len(s) < 1:
                raise TypeError("В ФИО должна быть хотя бы одна букова")
            if len(s.strip(letters)) != 0:
                raise TypeError("В ФИО можно использовать только буквы")

    def verify_old(cld, old):
        if type(old) != int or old < 14 or old > 120:
            raise TypeError(
                'Возраст должен быть в диапозоне [14:120] и быть целым')

    def verify_weight(cld, weight):
        if type(weight) != float and weight < 20:
            raise TypeError('Вес должен быть числом и больше 20')

    def verify_ps(cld, ps):
        if type(ps) != str:
            raise TypeError(
                'Не бывает такого короткого паспорта! >О')

    @property
    def fio(self):
        return self.__fio

    @property
    def old(self):
        return self.__old

    @old.setter
    def old(self, old):
        self.verify_old(old)
        self.__old = old

    @property
    def passport(self):
        return self.__ps

    @passport.setter
    def passport(self, ps):
        self.verify_ps(ps)
        self.__ps = ps

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, weight):
        self.verify_ps(weight)
        self.__weight = weight

    @old.deleter
    def old(self):
        del self.__old


p = Person('Иван Иванов Иванов', 'Иван', 28, '23424 2342', 70.8)


class ReadIntX:
    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        self.verify_coord(value)
        print(f'__set__: {self.name} = {value}')
        setattr(instance, self.name, value)

'''
'''

class Integer:

    @classmethod
    def verify_coord(cls, coord):
        if type(coord) != int:
            raise TypeError('Координаты должны быть целыми')

    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        self.verify_coord(value)
        print(f'__set__: {self.name} = {value}')
        setattr(instance, self.name, value)


class Point3D:
    xr = ReadIntX()
    x = Integer()
    y = Integer()
    z = Integer()

    def __init__(self, x, y, z):
        self._x = x
        self._y = y
        self._z = z


p = Point3D(45, 'f', 43)
print(p.x)
p.__dict__['xr'] = 10
print(p.xr)
print(p.__dict__)
'''


class Counter:
    def __init__(self):
        self.__counter = 0

    def __call__(self, step=1, *args, **kwargs):
        print('__call__')
        self.__counter += step
        return self.__counter


class StripChars:
    def __init__(self, chars):
        self.__chars = chars

    def __call__(self, *args, **kwargs):
        if not isinstance(args[0], str):
            raise ValueError('Аргумент не строка!')
        return args[0].strip(self.__chars)


'''

class Derivate:
    def __init__(self, func):
        self.__fn = func

    def __call__(self, x, dx=0.0001, *args, **kwargs):
        return (self.__fn(x+dx) - self.__fn(x))/dx

    @Derivate
    def df_sin(x):
        return math.sin(x)
'''


class Cat:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'{self.__class__}: {self.name}'

    def __str__(self):
        return f'{self.name}'


class Point:
    def __init__(self, *args):
        self.__coords = args

    def __len__(self):
        return len(self.__coords)

    def __abs__(self):
        return list(map(abs, self.__coords))  # Делаем списочек


class Clock:
    __Day = 86400

    def __init__(self, seconds: int):
        if not isinstance(seconds, int):
            raise TypeError('Секунда = число!')
        self.seconds = seconds % self.__Day

    def get_time(self):
        s = self.seconds % 60
        m = (self.seconds // 60) % 60
        h = (self.seconds // 3600) % 24
        return f'{self.__get_formatted(h)}:{self.__get_formatted(m)}:{self.__get_formatted(s)}'

    def __add__(self, other):
        if not isinstance(other, (int, Clock)):
            raise TypeError('Правый операнд должен быть int или Clock')
        sc = other if isinstance(other, int) else other.seconds
        return Clock(self.seconds + sc)

    def __radd__(self, other):
        return self + other

    def __iadd__(self, other):
        print("__iadd__")
        if not isinstance(other, (int, Clock)):
            raise TypeError('Правый операнд должен быть int или Clock')
        sc = other if isinstance(other, int) else other.seconds
        self.seconds += sc
        return self

    @classmethod
    def __get_formatted(cls, x):
        return str(x).rjust(2, '0')


c1 = Clock(1000)
print(c1.get_time())
c2 = Clock(2000)
c3 = Clock(3000)
c4 = 100 + c1
c1 += 100
print(c4.get_time())

# __sub__ вычитание -
# __mul__ сложение +
# __floordiv__ целочисленное деление //
# __mod__ деление с осттатком %
