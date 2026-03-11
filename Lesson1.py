# HFEGebf
# jshcj

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
a.create_acc('Lock228', 123)
a.create_acc('Lock228', 123)
print(a.reg)

a.create_acc('Okak', 22546)

a.enter_in_acc('FEfe', 1233)
a.enter_in_acc('Lock228', 123)

a.rename_acc('Lock228', 'Open31')

a.enter_in_acc('FEfe', 1233)
a.enter_in_acc('Open31', 123)

a.get_logs()

b = GAME()
b.win_the_match('Open31', 100, 121)
b.check_records('Open31')
