"================================Comprehensions=================================="
# comprehension - это генератор, с помощью которого мы можем создавать последовательности используя цикл for в одну строку

# структура
# результат for элемент in последовательность
# i for i in list1
# результат for элемент in последовательность if фильтр -- фильтр
# i for i in list1 if i %2 == 0
# тело1 if условие else тело for элемент посследовательность -- условие
# 'четное' if i % 2 == 0 else 'нечетное' for i in range(1, 11)

comprеhеnsion = (i for i in range (1,6))
print(comprеhеnsion)# <generator object <genexpr> at 0x0000016E0BDEC940>
# генератор - итерируемый объект который не хранит в себе полностью всю последовательность данных, а создает их когда требуется

#print(next(comprеhеnsion))
#print(next(comprеhеnsion))

# next() - функция, в которой запрашивает у генератора текущий элемент, и генератор создает следующий элемент


"============================================================================"
list_compehension = list((i ** 2 for i in range(1, 11)))
print(list_compehension)# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
list_compehension2 = [i ** 2 for i in range(1, 11)]
print(list_compehension2)# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# a = [i for i in range(1, 51) if i % 2 != 0]
# print(a)

b = ['hello' for i in range(1,6)]
print(b)# ['hello', 'hello', 'hello', 'hello', 'hello']

c = ['четное'if i % 2 == 0 else 'нечетное' for i in range(10)]
print(c)

v = [5,'hello', 7, 4, 5, 7 ,9, 'ADA', 'world', 'courses']
d = [i for i in v if type(i) == str]
print(d)# ['hello', 'ADA', 'world', 'courses']

"===========================Dict comprehensions========================"
# dict_ = dict( (i, i ** 2 ) for i in range(1, 11))
# print(dict_)# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}

# dict_ = {i: i ** 2 for i in range(1, 11)}
# print(dict_)

# Дан словарь, создайте его копию при помощи comprehension
# pon = {1:'a', 2:'b', 3:'c'}
# mon = {keys:values for keys, values in pon.items()}
# print(mon)

#Дан словарь, поменяйте ключи со значениями используя comprehension

dict4  = {1:'a', 2:'b', 3:'c'}
pon = {value: key for key, value in dict4.items()}
print(pon)

# for key, value in dict4.items():
#     dict[value] = key
# print(dict4)

# Дан словарь где значение - списки с числами, создайте словарь, где значениями будут суммы этих чисел
# dict1 = {
#      "a":[1,2,3,4],
#      "b":[10,15,16,17],
#      "c":[1,2,54]
# }
# dict2 = {key:sum(value) for key, value in dict1.items()}
# print(dict2)

"=========================Вложенные Comprehenshion======================"
# Создайте словарь где ключами будут числа от одног до 5 а значениями списки с числами от 1 ло этого числа
#{1: {1}, 2: {1, 2}, 3: {1, 2, 3}, 4: {1, 2, 3, 4}, 5: {1, 2, 3, 4, 5}}
# dict1 = {}
# for i in range(1, 6):
#     key = i
#     value = {j for j in range(1, i+1)}
#     dict1[key] = value
# print(dict1)

# dict2 = {i: [j for j in range(1, i+1)] for i in range(1,6)}
# print(dict2)

# создать список состоящий из 10 списков, в каждом из которых строка 'hello world' повторяется по 5 раз
#[['hello world', 'hello world', 'hello world', 'hello world', 'hello world'], ['hello world', 'hello world', 'hello world', 'hello world', 'hello world'], ['hello world', 'hello world', 'hello world', 'hello world', 'hello world'], ['hello world', 'hello world', 'hello world', 'hello world', 'hello world'], ['hello world', 'hello world', 'hello world', 'hello world', 'hello world'], ['hello world', 'hello world', 'hello world', 'hello world', 'hello world'], ['hello world', 'hello world', 'hello world', 'hello world', 'hello world'], ['hello world', 'hello world', 'hello world', 'hello world', 'hello world'], ['hello world', 'hello world', 'hello world', 'hello world', 'hello world'], ['hello world', 'hello world', 'hello world', 'hello world', 'hello world']]
# list1 = []

# for i in range(10):
#      inner_list = []
#      for j in range(5):
#           inner_list.append('hello world')
#      list1.append(inner_list)

# print(list1)

# list2 = [['hello' for i in range(5)] for i in range(10)]
# print(list2)

# Создайте список состоящий из 10 списков в которых юудут число от 1 до 5

# list1 = [[i for i in range(1, 6)] for i in range(10)]
# print(list1)
# Создвйте словарь где ключами будут числа от 1 до 5, а значениями будут словари в котором ключами будут числа от 1 до этого, а значениями будут списки от 1 до этого числа

# dict2 = {
#     i:{
#         j:[h for h in range(1, j + 1)] for j in range(1, i + 1) 
#         } 
#         for i in range(5)}
# print(dict2)

# dict2 = {}
# for i in range(1, 6):
#     inner_dict = {}
#     for j in range(1, i+1):
#         list_ = []
#         for k in range(1, j+1):
#             list_.append(k)
#         inner_dict[i] = list_
#     dict[i] = inner_dict

# print(dict2)

# Дан словарь:
#dict1 = {"Sedan": 1500, "SUV": 2000, "Pickup": 2500, "Miivan": 1600, "Vann": 2400, "Semi": 13600, "Bicycle": 7, "Motorcycle": 110}
# Создайте dict2:
# - ключи должны юытьте же, что и в 1 словаре, но каждый символ i замените на ''
# - значение должно быть количество повторений символо i в этом ключе

dict1 = {"Sedan": 1500, "SUV": 2000, "Pickup": 2500, "Miivan": 1600, "Vann": 2400, "Semi": 13600, "Bicycle": 7, "Motorcycle": 110}
dict2 = {key.replace('i',''):key.count('i') for key in dict1}
print(dict2)



# Используя приведенный словарь dict_, создайте список из id, 
# которые хранятся под ключом comments. Берите только те комментарии, 
# количество которых больше 3

dict_ = {
    'Dasha': {
        'likes': 15,
        'comments': [
            {'id': 1, 'text': 'some text'},
            {'id': 2, 'text': 'some text'},
        ],
        'rating': 2
    },
    'Luna': {
        'likes': 12,
        'comments': [
            {'id': 1, 'text': 'some text'},
            {'id': 2, 'text': 'some text'},
            {'id': 3, 'text': 'some text'},
        ],
        'rating': 1
    },
    'Rena': {
        'likes': 26,
        'comments': [
            {'id': 1, 'text': 'some text'},
            {'id': 2, 'text': 'some text'},
            {'id': 3, 'text': 'some text'},
            {'id': 4, 'text': 'some text'},
            {'id': 5, 'text': 'some text'},
            {'id': 6, 'text': 'some text'},
        ],
        'rating': 2
    }
}

comment_ids = [i['id'] for i in dict_.values() if len(i['comments']) > 3 for j in j['comments']]
print(comment_ids)

