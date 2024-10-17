"========================Словари=========================="
# Словарь 9 это изменяемый, итерируемый, неупорядочный, неиндксируемый тип данных, для хранения данных в парах (ключ:значение)

user = {
     "name": 'Nikita',
     'country': 'Kyrgyzstan',
     'last_name': 'Grebnev',
}

print(user)
print(user['name'])

# Ключами в словаре могут быть только неизменяемые типы данных
# user2 = {
#     'login':'ngrebnev',
#     ['password']: 'hello world' #TypeError: unhashable type: 'list'
# }


dict1 = {'a': 1, 'b':2, 'c':3, 'a':4}
print(dict1)# 4 (если ключт одиннаковые, сохранится только последнее значение)
#print(dict1['hello'])# KeyError: 'hello'

"==========================Создание словарей=============================="
#1
users = {
    'name': 'nikita',
    'password': '1'
}

#2
dict2 = {}
print(dict2)
dict2['name'] = 'Nikita'
print(dict2)
dict2['password'] = hash('nikita123')
print(dict2)

"===============================Методы словаря=================================="
#get() - это метод который возвращает значеник по ключу, если такого ключа не то возвращает None

print(dict2.get('password'))
print(dict2.get('name'))

# pop() - удаляет пару по ключу и возвращает значение
dict4 = {'a': '4', "b": "2"}
popped = dict4.pop ('b')
print(popped)
print(dict4)

#popitem() - удаляет последнюю и возвращает ее
dict_ = {1: 'a', 2: 'b', 3: 'a'}
popped = dict_.popitem()
print(popped)
print(dict_)
dict_.popitem()
dict_.popitem()
print(dict1)

# print(dir(dict))

#update() - расширяет словарь парами из второго словаря
dict1 = {1: 'a', 'b': 3}
dict2 = {'name': 'nikita', 'last_name': 'grebnev'}
dict1.update(dict2)
print(dict1)
print(dict2)

# clear() - очищает полностью словарь
dict1.clear()
dict2.clear()
print(f'dict2 {dict2}')
print(f'dict1 {dict1}')

"""
keys, values, items

keys - метод, который возвращает все ключи из словаря
values - метод, который возвращает все значения из cловаря 
items - метод, кторый возвращает и ключи и значения
"""
"===========================Итерирование словарей============================="

user = {
    'name': 'Amir',
    'last_name': 'Zakov',
    'age': '6986749579036576 годиков'
}


print(user.keys())#dict_keys(['name', 'last_name', 'age'])
print(user.values())#dict_values(['Amir', 'Zakov', '6986749579036576'])
print(user.items())#dict_items([('name', 'Amir'), ('last_name', 'Zakov'), ('age', '6986749579036576')])



for key in user:
    print(key)
    # при итерации словаря будут приходить ключи

for key in user.keys():
    print(key)
    # при итераций dict_keys тоже приходят ключи


for value in user.values():
    print(value)
    # при итераций dict_values приходит только значение

for key, value in user.items():
    print(f'Ключ: {key}, Значение: {value}')

# вам дан словарь
dict1 = {"a":1, "b":2, "c":3}
# создайте новый словарь, поменяв ключи со значениями
# {1:"a", 2:"b", 3:"c"}
dict2 = {}

for key, value in dict1.items():
    dict2[value] = key
print(dict2)
#{1: 'a', 2: 'b', 3: 'c'}

