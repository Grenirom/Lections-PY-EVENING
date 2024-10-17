# "==============================================Функции=================================="
# # функция - это именованный блок кода. который может принимать аргументы и возвращать результат

# def my_sum(x, y):
#     return x + y

# # print(my_sum(10, 10))
# # result = my_sum(20, 20)
# # print(result)

# def my_len(obj):
#     count = 0
#     for element in obj:
#         count += 1
#     return count

# list1 = [1, 2, 3, 4, 5, 6, True, False, [1,2,3]]
# print(my_len(list1))
# print(my_len('hello'))

# a = 'hello'
# count = 0
# for element in a:
#     count += 1
# print(count)


# """
# DRY - dont repeat yourself - функции соблюдают этот принцип
# """

# "=============================================Аргументы и параметры=============================="
# # Параметры - переменные внутри функции, значения которым мы задаем при определении функции (когда пишем def название_функции(параметры))
# # аргументы - переменные, которые мы передаем при вызове функции (my_len(аргументы))

# # def my_len(obj): -- obj - параметр
# #     count = 0
# #     for element in obj:
# #         count += 1
# #     return count
# # print(my_len(list1)) -- list1 - это аргумент

# "=======================================Виды параметров=================================="
# """
# 1) обязательные
# 2) не обязательные
#     2.1) с дефолтным значение
#     2.2) *args (все позиционные аргументы, которые не попали в обязательные, и с дефолтным значением, хранятся в tuple)
#     2.3) **kwargs (все лишние именованные аргументы, хранятся в dict)
# """
# "=====================================Виды аргументов==========================================="
# """
# 1) позиционные (по позиции)
# 2) именнованные (по названию (параметр=значение))
# """

# def add_or_add_10(num1, num2=10):
#     """
#     Складывает 2 числа
#     Если второе число не передать, сложит первое с 10
#     """
#     return num1 + num2

# print(add_or_add_10(15, 15)) # Аргументы позиционные
# print(add_or_add_10(num1=22, num2=21)) # Аргументы именованные
# # print(add_or_add_10(num2=10)) TypeError (не указали обязательный позиционный аргумент)
# print(add_or_add_10(num2=12, num1=12)) # 24

# "=======================================* и **========================================"
# # * - list, tuple
# list1 = list(range(1, 11)) # [1,2,3,4,5,6,7,8,9,10]
# print(list1)

# list1 = [range(1, 11)] #[range(1, 11)]
# print(list1)

# list1 = [*range(1, 11)]
# print(list1) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# dict1 = {1: 'a', 2: 'b', 3: 'c'}
# print(dict1)

# dict2 = {**dict1} # {1: 'a', 2: 'b', 3: 'c'}
# print(dict2)

# list1 = [*dict1]
# print(list1) # [1, 2, 3]

# def func(a, b=10, *args, **kwargs):
#     print('a - ', a)
#     print('b - ', b)
#     print('args - ', args)
#     print('kwargs - ', kwargs)

# func(12, 120, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, name='nikita', city='bishkek', country='Kyrgyzstan')

# "============================================lambda=============================="
# # lambda - Анонимная функция, которая записывается в одну строку
# lambda_func = lambda x: x ** 10
# print(lambda_func(10))

# "===================================Калькулятор======================================="

# calculator = {
#     '+': lambda num1, num2: num1 + num2,
#     '-': lambda num1, num2: num1 - num2,
#     '*': lambda num1, num2: num1 * num2,
#     '**': lambda num1, num2: num1 ** num2,
#     '/': lambda num1, num2: num1 / num2,
#     '//': lambda num1, num2: num1 // num2,
#     '%': lambda num1, num2: num1 % num2
# }

# def main():
#     try:
#         num1 = int(input('Введите первое число: '))
#         num2 = int(input('Введите второе число: '))
#         operator = input('Введите операцию: ')
#         func = calculator[operator]
#         result = func(num1, num2)
#         print(f'{num1} {operator} {num2} = {result}')
#     except ValueError:
#         print('Вы написали не число')
#     except KeyError:
#         print('Такой операции нет')
#     except ZeroDivisionError:
#         print('На ноль делить нельзя')

# while True:
#     main()
#     inp = input('Завершить? (yes/no)')
#     if inp.lower() == 'yes':
#         break


db = [
    {'name': 'Nikita', 'password': hash('nikita123321')},
    {'name': 'Nikita2', 'password': hash('123321123')}
]

def in_database(name):
    for user in db:
        if user['name'] == name:
            return True
    return False

def register(name, password, password_confirm):
    if in_database(name):
        raise Exception('Пользователь с таким именем уже существует')
    if password != password_confirm:
        raise Exception('Пароли не совпали')
    user = {'name': name, 'password': hash(password)}
    db.append(user)
    return 'Вы успешно зарегистрировались'

def login(name, password):
    if not in_database(name):
        raise Exception('Пользователь не найден')
    for user in db:
        if user['name'] == name:
            if user['password'] != hash(password):
                raise Exception('Пароль не верный!')
    return 'Вы успешно вошли в систему'

from decorators import time_decorator

@time_decorator
def main():
    print('Добро пожаловать!')
    while True:
        try:
            action = input('Register:1, Login:2, Quit:3')

            if action == '3':
                break
            elif action == '1':
                name = input('Введите имя: ')
                password1 = input('Введите пароль: ')
                password2 = input('Подтвердите пароль: ')
                print(register(name, password1, password2))
            elif action == '2':
                name = input('Введите имя: ')
                password = input('Введите пароль: ')
                print(login(name, password))
            else:
                print('Не корректный выбор!')
        except Exception as error:
            print(error)

main()

# 1)Спросите у пользователя 5 чисел добавьте их в SET и скажите какое самое маленькое число он ввел. 

# def smallest():
#     numbers = set()
#     for _ in range(5):
#         num = int(input('Введите число'))
#         numbers.add(num)
#     print(f'smallest {min(numbers)}')

# smallest()

# 2) Вы работаете в Банке и пишите программу которая считает % для кредита. Спросите у пользователя сумму займа(не меньше 100 000) и посчитайте сколько нужно будет вернуть если процент = 7.89, результат округлите до 2 чисел после точки. Формула подсчёта переплаты: Сумма * (% / 100) 

def credit():
    zaim = float(input('Введите сумму займа (не менее 100к)'))
    if zaim < 100000:
        print('Сумма займа не должна быть меньше 100к')
    percent = 7.89
    total_credit = zaim + (zaim * (percent / 100))
    return round(total_credit, 2)

# print(credit())

# 3) Запросите у пользователя ввести текст с цифрами, найти цифры и преобразовать их в целое число и вывести на экран. 

# def find_nums():
#     str_ = input('Введите текст с цифрами')
#     list_ = [int(x) for x in str_ if x.isdigit()]
#     return list_

# print(find_nums())

# 4) Создайте функцию, которая выполняет следующее действие: Пользователь вводит количество месяцев и лет. Вывести на экран количество дней за это время. Считать, что в каждом месяце 30 дней; 

def find_days():
    years = int(input('Введите количество лет'))
    months = int(input('Введите количество месяцев'))
    days = (years * 365) + (months * 30)
    return days

# print(find_days())
# 5) Создайте функцию, которая возвращает словарь, где ключами будут числа от 1 до 10, а значениями эти же числа, возведенные в куб.

# def cube_dict():
#     cube = {i: i**3 for i in range(1, 11)}
#     return cube

# print(cube_dict())

# 6) Написать функцию, которая высчитывает сумму чисел от 1 до 50 и возвращает результат.

# def sum_nums():
#     # return sum(range(1, 51))
#     total_ = 0
#     for i in range(1, 51):
#         total_ += i
#     return total_

# print(sum_nums())

# 11) Напишите функцию is_palindrome, которая принимает строку и возвращает True, если строка является палиндромом, и False в противном случае. Палиндром - строка которая справа налево, и слева на право читается одинаково. Например "Анна", "Казак" 

def is_palindrome(text):
    return text == text[::-1]

print(is_palindrome('anna'))

# print('hello'[::-2])

