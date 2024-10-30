# '=============================================JSON======================================'
# # Javascript Object Notation - универсальный формат, в котором мы можем хранить данные в типах данных, понятных почти для всех языков программирования

# """
# Сериализация - Перевод с python объектов в JSON строку

# Десериализация - перевод из JSON строки в python объекты
# """

# import json

# """
# .dumps() - Метод для сериализации в json строку

# .dump() - метод для сериализации в json файл
# """

# user_data = {
#     'email': 'nikita@gmail.com',
#     'password': '123321',
#     'is_active': False,
#     'access': None
# }

# with open('user_data.json', 'w') as file:
#     json.dump(user_data, file)


# json_string = json.dumps(user_data)
# print('JSON строка:', json_string)

# """
# loads() - метод для десериализации с json строки

# load() - метод для десериализации с json файла
# """

# with open('user_data.json', 'r') as file:
#     python_data = json.load(file)
#     print(python_data, 'Десериализация')

# python_dict = json.loads(json_string)
# print(python_dict, 'С JSON строки')

import json
# Создайте JSON-объект, который содержит список продуктов, где каждый продукт — это словарь с названием, ценой и количеством. Запишите этот объект в файл products.json. для списка продуктов можете использовать этот объект
# products = [
#     {"name": "Laptop", "price": 1200, "quantity": 5},
#     {"name": "Mouse", "price": 25, "quantity": 50},
#     {"name": "Keyboard", "price": 70, "quantity": 20}
# ]


# with open('products.json', 'w') as file:
#     json.dump(products, file)


# Прочитайте содержимое файла products.json, увеличьте цену каждого продукта на 10%, затем запишите обновлённые данные обратно в файл. (для увеличения цены на 10% нужно умножить цену на 1.1)


# with open('products.json', 'r') as file1:
#     products = json.load(file1)

# for product in products:
#     product['price'] *= 1.1

# with open('products.json', 'w') as file2:
#     json.dump(products, file2)

# 7)  Прочитайте файл products.json, добавьте новый продукт в список и снова сохраните его в файл.

# new_product = {'name': 'iphone', 'price': 1200, 'quantity': 5}

# with open('products.json', 'r') as file:
#     products = json.load(file)

# products.append(new_product)

# with open('products.json', 'w') as file:
#     json.dump(products, file)

# 8) Создайте JSON-файл с данными о сотрудниках (имя, должность, зарплата), при этом некоторые значения могут быть None. Прочитайте этот файл и выведите на экран сотрудников с известной зарплатой.

# employees = [
#     {'name': 'Nikita', 'position': 'Manager', 'salary': 1500},
#     {'name': 'Ertay', 'position': 'Data-science engineer', 'salary': 2000},
#     {'name': 'Katana', 'position': 'Backend Developer', 'salary': None},
#     {'name': 'Tima', 'position': 'ML Engineer', 'salary': None},
# ]

# with open('employees.json', 'w') as file:
#     json.dump(employees, file)

# with open('employees.json', 'r') as file:
#     employees = json.load(file)

# for employee in employees:
#     if employee['salary'] is not None:
#         print(employee)

from datetime import date, timedelta

orders = [
    {
        "order_id": 1,
        "customer": "Alice",
        "date": str(date(2024, 1, 10)),
        "products": [
            {"name": "Laptop", "quantity": 1, "price": 1200},
            {"name": "Mouse", "quantity": 2, "price": 25},
            {"name": "Monitor", "quantity": 1, "price": 300},
            {"name": "Keyboard", "quantity": 1, "price": 70}
        ]
    },
    {
        "order_id": 2,
        "customer": "Bob",
        "date": str(date(2024, 1, 12)),
        "products": [
            {"name": "Monitor", "quantity": 1, "price": 300},
            {"name": "Keyboard", "quantity": 1, "price": 70}
        ]
    },
    {
        "order_id": 3,
        "customer": "Mariya",
        "date": str(date(2023, 12, 12)),
        "products": [
            {"name": "Monitor", "quantity": 2, "price": 300},
        ]
    },
        {
        "order_id": 4,
        "customer": "Marat",
        "date": str(date(2024, 8, 10)),
        "products": [
            {"name": "Mouse", "quantity": 122, "price": 25},
            {"name": "Monitor", "quantity": 12, "price": 300},
            {"name": "Keyboard", "quantity": 11, "price": 70}
        ]
    },
]

# 9) Создайте JSON-файл, который содержит информацию о разных заказах в интернет-магазине. Каждый заказ должен включать список продуктов, покупателя и дату заказа. Запишите эти данные в файл orders.json.

# with open('orders.json', 'w') as file:
#     json.dump(orders, file)

# 10)  Прочитайте файл orders.json и выведите информацию только о тех заказах, которые содержат более 2товаров.

with open('orders.json', 'r') as file:
    orders = json.load(file)

for order in orders:
    if len(order['products']) > 2:
        print(order)

# 11) Прочитайте файл orders.json и измените статус всех заказов с даты старше месяца на "доставлен". Запишите обновлённые данные обратно в файл.

# with open('orders.json', 'r') as file:
#     orders = json.load(file)


# month_ago = date.today() - timedelta(days=30)

# for order in orders:
#     order_date = date.fromisoformat(order['date'])

#     if order_date < month_ago:
#         order['status'] = 'delivered'

# with open('orders.json', 'w') as file:
#     json.dump(orders, file)

# 12) Прочитайте файл orders.json, посчитайте общее количество товаров, проданных за месяц, и общую сумму всех заказов. Выведите результаты на экран.

with open('orders.json', 'r') as file:
    orders = json.load(file)

total_quantity = 0
total_sales = 0

for order in orders:
    for product in order['products']:
        total_quantity += product['quantity']
        total_sales += product['quantity'] * product['price']

print(f'Общее количество проданного товара: {total_quantity}')
print(f'Общая сумма всех заказов: {total_sales}')
