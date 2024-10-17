"==================================================Декораторы============================================="
# Функция высшего порядка - функция, которая принимает в аргументы другую функцию, создает внутри себя функцию, вызывает функцию, возвращает функцию

# Декоратор - функция высшего порядка, которая нужна чтобы расширять функционал функции, не изменяя ее функционал (функция обертка)


# как пишутся декораторы

def time_decorator(func):
    def wrapper(*args, **kwargs):
        from datetime import datetime
        print(f'start: {datetime.now()}')
        func(*args, **kwargs)
        print(f'finish: {datetime.now()}')
    return wrapper

@time_decorator
def hello():
    print('Привет')

# hello()

def func_total_time(func):
    def wrapper(*a, **k):
        from datetime import datetime
        now = datetime.now()
        correct_format = now.strftime('%d.%m.%Y %H:%M')
        print(f'Функция запущена: {correct_format}')
        func(*a, **k)
    return wrapper

@func_total_time
def iterate_list(list_):
    for i in list_:
        print(i)
    
# iterate_list([1,1,1,1,1,1])


# def iter_decorator(num):
#     def inner_decorator(func):
#         def wrapper(*args, **kwargs):
#             for i in range(num):
#                 func(*args, **kwargs)
#         return wrapper
#     return inner_decorator

# @iter_decorator(100)
# def hello():
#     print('Hello')

# hello()

from time import time
# import requests

def benchmark(func):
    def wrapper(*args, **kwargs):
        start = time()
        func(*args, **kwargs)
        finish = time()
        total_time = finish - start
        print(f'Время выполнения функции: {total_time} секунд')
    return wrapper

@benchmark
def iter_range():
    count = 0
    for i in range(1, 1000001):
        count += i
    print(count)

# iter_range()


@benchmark
def fetch_webpage():
    webpage = requests.get('https://youtube.com')

fetch_webpage()
