# HFEGebf

from dataclasses import dataclass, field
from dataclasses import dataclass
import timeit
from datetime import datetime
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


'''
class Clock:
    __Day = 86400

    @classmethod
    def __verify_data(cls, other):
        if not isinstance(other, (int, Clock)):
            raise ArithmeticError('Правый операнд должен быть int или Clock')
        return other if isinstance(other, int) else other.seconds

    def __init__(self, seconds: int):
        if not isinstance(seconds, int):
            raise TypeError('Секунда = число!')
        self.seconds = seconds % self.__Day

    def get_time(self):
        s = self.seconds % 60
        m = (self.seconds // 60) % 60
        h = (self.seconds // 3600) % 24
        return f'{self.__get_formatted(h)}:{self.__get_formatted(m)}:{self.__get_formatted(s)}'

    def __eq__(self, other):
        sc = __verify_data(other)
        return self.seconds == sc

    def __lt__(self, other):
        sc = __verify_data(other)
        return self.seconds < sc

    def __add__(self, other):
        sc = __verify_data(other)
        return Clock(self.seconds + sc)

    def __le__(self, other):
        sc = __verify_data(other)
        return self.seconds <= sc

    def __radd__(self, other):
        return self + other

    def __iadd__(self, other):
        print("__iadd__")
        sc = __verify_data(other)
        self.seconds += sc
        return self

    @classmethod
    def __get_formatted(cls, x):
        return str(x).rjust(2, '0')
'''


# __sub__ вычитание -
# __mul__ сложение +
# __floordiv__ целочисленное деление //
# __mod__ деление с осттатком %

# == __eq__
# != __ne__
# < __lt__
# <= __le__


class Point2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))  # Один hash на двоих

    def __len__(self):
        print("__len__")
        return self.x * self.x + self.y * self.y

    def __bool__(self):
        print("__booll__")
        return self.x == self.y


'''
p1 = Point2(1, 2)
p2 = Point2(1, 2)

print(hash(p1), hash(p2))
print(p1 == p2)

d = {}
d[p1] = 1
d[p2] = 2

print(d)
'''


class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = list(marks)

    def __getitem__(self, item):
        if not isinstance(item, int):
            raise IndexError("Индекс долэен быть целым")
        if 0 <= item <= len(self.marks):
            return self.marks[item]
        else:
            raise IndexError("Неверный индекс")

    def __setitem__(self, key, value):
        if not isinstance(key, int) or key < 0:
            raise IndexError("Неверный индекс")
        if key >= len(self.marks):
            off = key + 1 - len(self.marks)
            self.marks.extend([None] * off)
        self.marks[key] = value

    def __delitem__(self, key):
        if not isinstance(key, int) or key < 0:
            raise IndexError("Неверный индекс")
        del self.marks[key]


'''
s1 = Student('Ivan', [3, 3, 4, 5, 4, 2, 3])
print(s1[4])
s1[99] = 5
del s1[99]
print(s1[98])
'''


class FRange:
    def __init__(self, start=0.0, stop=0.0, step=0.1):
        self.start = start
        self.stop = stop
        self.step = step
        self.value = self.start - self.step

    def __next__(self):
        if self.value + self.step <= self.stop:
            self.value += self.step
            return self.value
        else:
            raise StopIteration

    def __iter__(self):
        self.value = self.start - self.step
        return self


class FRange2D:
    def __init__(self, start=0.0, stop=0.0, step=0.1, rows=5):
        self.fr = FRange(start, stop, step)
        self.rows = rows

    def __iter__(self):
        self.value_rows = 0
        return self

    def __next__(self):
        if self.value_rows < self.rows:
            self.value_rows += 1
            return iter(self.fr)
        else:
            raise StopIteration


# 1
'''

class User:

    def __init__(self, name_age):
        name, age = self.split_it(name_age)
        self.name = name
        self.age = age

    @classmethod
    def split_it(cls, name_age):
        name_age = name_age.split(';')
        name = name_age[0]
        age = name_age[1]
        return name, age


us1 = User('ОЛег;32')

print(f"Имя: {us1.name}")
print(f"Возраст: {us1.age}")

# 2


class Coordinate:
    def __init__(self, x, y):
        self.verify_x(x)
        self.verify_y(y)

        self.__x = x
        self.__y = y

    @classmethod
    def verify_x(cls, x):
        if type(x) != int and type(x) != float:
            raise TypeError('x должен быть int или floatt!')

    @classmethod
    def verify_y(cls, y):
        if type(y) != int and type(y) != float:
            raise TypeError('y должен быть int или floatt!')

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @x.setter
    def x(self, x):
        self.verify_x(x)
        self.__x = x

    @y.setter
    def x(self, y):
        self.verify_y(y)
        self.__y = y


coord1 = Coordinate(1.6, 23)
# coord1 = Coordinate('gd', 23)

#


class Multiplier:
    def __init__(self, n):
        self.n = n

    def __call__(self, mnosh):
        return mnosh*self.n


m = Multiplier(11)
m2 = Multiplier(100)
print(m(4))
print()
print(m2(6))


# 4

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):  # Ето +
        if isinstance(other, Vector):
            return self.x + other.x, self.y + other.y
        if isinstance(other, (int, float)):
            return self.x + other, self.y + other

    def __sub__(self, other):  # Ето -
        if isinstance(other, Vector):
            return self.x - other.x, self.y - other.y
        if isinstance(other, (int, float)):
            return self.x - other, self.y - other

    def __mul__(self, other):  # Ето *
        if isinstance(other, Vector):
            return self.x * other.x, self.y * other.y
        if isinstance(other, (int, float)):
            return self.x * other, self.y * other

    def __rmul__(self, other):
        return self * other

    def __str__(self):  # Ето красивишно
        return (f"Вектор = ({self.x},{self.y})")


v1 = Vector(1, 3)
v2 = Vector(2, 3)

print('v1 + v2 =', v1 + v2)
print('v1 - v2 =', v1 - v2)
print('v1 * v2 =', v1 * v2)

print('')

print('v1:', str(v1))
print('v2:', str(v2))

print('')

print(v2 * v2)
print(v1 - v1)
print(v2 + v1)

print('')

print(v1 + 1211)
print(v1 - 231)
print(23424 * v2)

# Вчерашнее


class Inventory:
    def __init__(self, weapon, armor, potions, potions_quantity, items):
        self.weapon = weapon
        self.armor = armor
        self.potions = potions
        self.potions_quantity = potions_quantity
        self.items = items if isinstance(items, list) else []

    def _to_dict(self):
        return {"weapon": self.weapon,
                "armor": self.armor,
                "potions": self.potions,
                "potions quantity": self.potions_quantity,
                "items": self.items
                }


class Player:
    def __init__(self, username, email, level, rang):
        self.username = username
        self.__email = email
        self.created_at = datetime.now()
        self.level = level
        self.rang = rang

    def _to_dict(self):
        return {"username": self.username,
                "email": self.__email,
                "created_at": self.created_at.isoformat(),
                "profile": {
                    "level": self.level,
                    "rang": self.rang
                }
                }


class GameSession:
    def __init__(self, experience):
        self.experience = experience
        self.time_session = datetime.now()

    def _to_dict(self):
        return {"experience": self.experience,
                "time_session": self.time_session.isoformat()}

'''
'''
p1 = Player('Амелия', 'sobaka@okak.com', 11, 5)
inv1 = Inventory('Меч', 'Кожаные ботинки', 'Зелье здоровья',
                 '10', ['Рог единорога', 'Зуб акулы'])
gm1 = GameSession(1090)

all_data = {
    "player": p1._to_dict(),
    "inventory": inv1._to_dict(),
    "game_session": gm1._to_dict()
}

with open("player_data.json", "w", encoding="utf-8") as json_file:
    json.dump(all_data, json_file, ensure_ascii=False, indent=4)

with open("player_data.json", "r", encoding="utf-8") as reading_file:
    loaded_data = json.load(reading_file)
    print("\nДанные успешно прочитаны из player_data.json:")
    print(json.dumps(loaded_data, ensure_ascii=False, indent=4))
'''


class Geom:
    __name = "Geom"

    def __init__(self, x1, x2, y1, y2):
        print(f'Init Geom для {self.__class__}')
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y1 = y2

    def draw(self):
        print('Рисование примитива')

    def __verify_coord(self, coord):  # Приватный метод
        return 0 <= coord <= 100


class Line(Geom):  # Наследование
    name = 'Line'

    def get_coords(self):
        return (self._x1, self._x2)

    def draw(self):
        print('Рисование Line')


class Rect(Geom):

    def __init__(self, x1, x2, y1, y2, fill=None):
        # Geom.__init__(self, x1, x2, y1, y2) Не лучшая практика
        super().__init__(x1, x2, y1, y2)
        print('Init Rect')
        self._fill = fill

    def draw(self):
        print('Рисование Rect')


class Vector(list):
    def __str__(self):
        return ''.join(map(str, self))


class Geom20:
    def get_pr(self):
        raise NotImplementedError('В дочернем классе должен быть get_pr()!')


class Rectangle(Geom20):
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def get_pr(self):
        return 2*(self.w + self.h)


class Square(Geom20):
    def __init__(self, a):
        self.a = a

    def get_pr(self):
        return self.a * 4


class Triangle(Geom20):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c


class MixinLog2():
    def __init__(self):
        super().__init__()
        print('mixin2')


class MixinLog():
    ID = 0

    def __init__(self):
        print('mixin')
        self.ID += 1
        self.id = self.ID

    def save_sell_log(self):
        print(f'Товар {self.id} продан')

    def print_info(self):
        print('пишу важни дату')


class Goods:
    def __init__(self, name, weight, price):
        super().__init__()
        print('init Goods')

        self.name = name
        self.weight = weight
        self.price = price

    def print_info(self):
        print(f'{self.name}, {self.weight}, {self.price}')


# Как тут стоит наследственность, так и будет отрабатывать оператор super()
class NoteBook(Goods, MixinLog, MixinLog2):
    def print_info(self):
        MixinLog.print_info(self)


'''
class Point2D:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.__lenght = (x*x + y*y) ** 0.5

    def calc(self):
        self.x += 1
        del self.y
        self.y = 0

    __slots__ = ('x', 'y', '__lenght')

    MAX_COORD = 100

    @property
    def lenght(self):
        return self.__lenght

    @lenght.setter
    def lenght(self, value):
        self.__lenght = value


class Point3D(Point2D):
    __slots__ = 'z',

    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z

'''
# 1 Банкротскво


class Payment:
    def pay(self, amount):
        raise NotImplementedError("Метод должен быть переопределен")


class SberPay(Payment):
    def pay(self, amount):
        super().__init__()
        print(f"Оплата {amount} через Сбер")


class TinkoffPay(Payment):
    def pay(self, amount):
        super().__init__()
        print(f"Оплата {amount} через Тинькофф")


'''
sber = SberPay()
tb = TinkoffPay()

# Все деньги с карточек депаем через список
peypay = [sber, tb, sber, tb, tb, tb]

for p in peypay:  # Полиморфим на максималках
    p.pay(100)
    '''

# 2 Алё


class Phone:
    def call(self, number):
        pass


class Camera:
    def take_photo(self):
        pass


class Smartphone(Camera, Phone):
    def call(self, number):
        super().__init__()

    def take_photo(self):
        super().__init__()


# 3

class Point2D1:
    __slots__ = ('x', 'y', 'color')

    def __init__(self, x, y):
        self.x = x
        self.y = y


# 4

class Point2D2:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    @property
    def length(self):
        return self.x+self.y

    __slots__ = ('x', 'y')


class Point3D(Point2D2):

    def __init__(self, pt, z):
        self.x = pt.x
        self.y = pt.y
        self.z = z

    @property
    def length(self):
        return self.x+self.y+self.z

    __slots__ = ('z', 'color')


# p2.color = 'blue'
# p3.color = 'blue'


class Man:
    title = 'Объект класса для title'
    photo = 'Объект класса для photo'
    ordering = 'Объект класса для ordering'

    def __init__(self, user, psw):
        self._user = user
        self._psw = psw
        self.meta = self.Meta(user + '@' + psw)

    class Meta:
        ordering = ['id']

        def __init__(self, acess):
            self.acess = acess


class B1:
    pass


class B2:
    pass


def method1(self):
    print(self.__dict__)


A = type('Point', (B1, B2), {'Mx': 100, 'Mn': 0,
         'method1': method1, 'method2': lambda self: self.Mx})

# Определяем функцию и методы прямо без явного объявдения класса META-класс


def create_class_point(name, base, attrs):
    attrs.update({'Mx': 100, 'Mn': 0})
    return type(name, base, attrs)


class Point2(metaclass=create_class_point):
    def get_coords(self):
        return (0, 0)


class Meta(type):
    def __new__(cls, name_class, base, attrs):
        attrs.update({'Mx': 100, 'Mn': 0})
        return type.__new__(cls, name_class, base, attrs)


class Point3(metaclass=Meta):
    def get_coords(self):
        return (0, 0)


class Meta2(type):
    def create_local_attrs(self, *args, **kwargs):
        for key, value in self.class_attrs.items():
            self.__dict__[key] = value

    def __init__(cls, name_class, base, attrs):
        cls.class_attrs = attrs
        cls.__init__ = Meta.create_local_attrs


class Thing:
    def __init__(self, name, weight, price):
        self.name = name
        self.weight = weight
        self.price = price

    def __repr__(self):
        return f"Thing: {self.__dict__}"


@dataclass
class ThingData:
    name: str
    weight: int
    price: float = 0
    dims: list = field(default_factory=list)

    def __eq__(self, other):
        return self.weight == other.weight


class Vector3D:
    def __init__(self, x: int, y: int, z: int):
        self.x = x
        self.y = y
        self.z = z
        self.lenght = (x*x + y*y+z*z)**0.5


@dataclass
class V3D:
    x: int = field(repr=False)
    y: int
    z: int = field(compare=False)
    # С помощью параметра compare запрещаем или разрешаем сравнивать переменные
    lenght: float = field(init=False, compare=False)

    def __post_init__(self):
        self.lenght = (self.x*self.x + self.y*self.y+self.z*self.z)**0.5


v = V3D(1, 2, 3)
v2 = V3D(1, 2, 5)

print(v)
print(v == v2)
