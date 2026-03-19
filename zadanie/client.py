import requests

my_products = [
    {'name': 'Ноутбук', 'price': 1000.0, 'stock': 5},
    {'name': 'Мышка', 'price': 50.0, 'stock': 2},
    {'name': 'Коврик', 'price': 10.0, 'stock': 10}
]

response = requests.post('http://172.16.153.182:8000/products/',
                         json={'name': 'Ноутбук', 'price': 1000.0, 'stock': 5})
print("Добавлен товар")

response = requests.post('http://172.16.153.182:8000/products/',
                         json={'name': 'Мышка', 'price': 50.0, 'stock': 2})
print("Добавлен товар")

response = requests.post('http://172.16.153.182:8000/products/',
                         json={'name': 'Коврик', 'price': 10.0, 'stock': 10})
print("Добавлен товар")


response = requests.get('http://172.16.153.182:8000/products/')
products_list = response.json()

print("Прайс-лист")
for p in products_list:
    if p['name'] == "Мышка":
        id_mish = p['id']
    print(
        f"ID: {p['id']}, name: {p['name']}, price: {p['price']}, stock: {p['stock']}")


for i in range(3):
    response = requests.post(
        'http://172.16.153.182:8000/buy/' + str(id_mish), params={'quantity': 1})

    if response.status_code == 200:
        print(f"Купля {i+1} мышки успешна")

    elif response.status_code == 400:
        print("Упс, мышки закончились!")
    else:
        print('бан')


response = requests.get('http://172.16.153.182:8000/stats/')

total_value = response.json().get('total_inventory_value')
print(f"Итоговая стоимость склада: {total_value}")
