"================================================Встроенные функции======================================"
# map, filter, reduce, zip, enumerate

# zip - соединяет несколько последовательностей (получаем генератор, в котором элементы - tuple)

list1 = [1, 2, 3, 4, 5]
list2 = ['a', 'b', 'c']
list3 = [10.1, 10.2, 20.6]

zipped = list(zip(list1, list2, list3))
print(zipped) # <zip object at 0x1004f3ec0> / [(1, 'a', 10.1), (2, 'b', 10.2), (3, 'c', 20.6)]

for element in zipped:
    print(element)

# (1, 'a', 10.1)
# (2, 'b', 10.2)
# (3, 'c', 20.6)

list4 = [1, 2, 3, 4, 5]
list5 = ['a', 'b', 'c', 'd', 'e']
dict_ = dict(zip(list4, list5))
print(dict_) # {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e'}
"===============================================Enumerate================================================"
# enumerate - нумерует последовательность (по дефолту начинает с 0) (так-же как и с zip() получаем генератор)

enumerated = enumerate('hello')
print(enumerated) # <enumerate object at 0x104cd7c40>

for element in enumerated:
    print(element)

# (0, 'h')
# (1, 'e')
# (2, 'l')
# (3, 'l')
# (4, 'o')

string = '[hello world'
print(dict(enumerate(string)))
# [(0, 'h'), (1, 'e'), (2, 'l'), (3, 'l'), (4, 'o'), (5, ' '), (6, 'w'), (7, 'o'), (8, 'r'), (9, 'l'), (10, 'd')]
"===================================================map============================================="
# map - функция, которая принимает в аргументы функцию и последовательность, и применяет эту функцию к элементам последовательности (записывает в новую последовательность результат функции, в которую передаются элементы последовательности)

# поменяйте тип данных элементов list_ со строк на числа
list_ = ['1', '229736423864872346239842894829374', '3', '4', '5']
mapped_list = list(map(int, list_)) # <map object at 0x1031e32e0>
print(mapped_list) # [1, 2, 3, 4, 5]

# создать новый список, элементы которого - квадраты элементов list1
list1 = [12, 13, 14, 15, 16, 17]
mapped_list = list(map(lambda x: x**2, list1))
# print(mapped_list) # [144, 169, 196, 225, 256, 289]

def to_2_degree(x):
    return x ** 2

print(list(map(to_2_degree, list1))) # [144, 169, 196, 225, 256, 289]
"===============================================Filter======================================"
# filter - Возвращает генератор с элементами, прошедшими фильтр (какое-то условие), принимает в себя : 1) функцию, 2) последовательность

list1 = [1, 0, -1, -23, -55, 15, 22]
# отфильтровать элементы списка, оставить только те, которые больше 0
filtered = list(filter(lambda x: x > 0, list1))
print(filtered)

list_ = list(range(1, 51))
# Отфильтровать list_, оставить только четные числа
filtered = list(filter(lambda x: x % 2 == 0, list_))
print(filtered)

users = [
    {'name': 'nikita', 'age': 10},
    {'name': 'nastya', 'age': 34},
    {'name': 'tima', 'age': 19}
]
# отфильтровать пользователей, оставить только тех, кому больше 18

solution1 = [user for user in users if user['age'] > 18]
print(solution1)

solution2 = list(filter(lambda user: user['age'] > 18, users))
print(solution2)
"=============================================reduce==============================="
from functools import reduce
# reduce - принимает функцию и последовательность, возвращает 1 результат (передаваемая функция должна обязательно принимать 2 аргумента)

list1 = list(range(1, 101))
result = reduce(lambda x, y: x + y, list1)
print(result) # 5050

string = 'hello'
res = reduce(lambda x, y: x + '%' + y, string)
print(res) # h%e%l%l%o
