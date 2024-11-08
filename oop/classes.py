"=====================================================OOP=============================================="
# OOП - Объектно ориентированное программирование (парадигма/стиль написания кода)
# Классы принято именовать при помощи CamelCase

# принципы ООП
"""
1) Наследование (Основной)
2) Инкапсуляция (Основной)
3) Полиморфизм (Основной)
4) Абстракция
5) Ассоциация
"""
class Person:
    # Переменные внутри класса - аттрибуты
    brain = 1 # аттрибут класса
    body = 1 # аттрибут класса
    legs = 2 # аттрибут класса
    arms = 2 # аттрибут класса

    # функции внутри класса - методы
    def __init__(self, name, age, last_name) -> None:
        # __init__ - метод, который будет добавлять в объект те аттрибуты. которые отличаются у разных объектов
        # self - ссылка на объект, который только что создался
        self.name = name
        self.last_name = last_name
        self.age = age
    
    def walk(self):
        return f'{self.name} ходит'
    
    def happy_birthday(self):
        self.age += 1
        return f'у пользователя {self.name} сегодня день рождения, исполнилось {self.age} лет'


    
nikita = Person('Nikita', 1, 'grebnev')
print(nikita) # <__main__.Person object at 0x1009faa80>
print(nikita.age) # 1
print(nikita.name) # nikita
nikita.walk() # Nikita ходит
print(nikita.walk) # <bound method Person.walk of <__main__.Person object at 0x104222e70>>
print(nikita.happy_birthday())
print(nikita.happy_birthday())
print(nikita.happy_birthday())
print(nikita.happy_birthday())
print(dir(nikita))
tima = Person('Tima', 21, 'Zhoroev')
print(tima.age)
print(tima.name)
print(tima.last_name)

nikita.hello = 'Hello'
print(nikita.hello)
# print(tima.hello)

"=============================================================Объектов================================================="
"""
объект, экземпляр, instance (инстанс) - синонимы, которые означают объект, созданный по шаблону класса
"""
"==================================================Аттрибуты и методы==================================================="
"""
Аттрибуты - переменные
методы - функции
"""
"========================================================================================================================="

class A:
    var1 = 'аттрибут(переменная) класса'

    def __init__(self) -> None:
        self.var2 = 'аттрибут(переменная) объекта'

    def __str__(self) -> str:
        return 'Объект от класса A'

obj1 = A()
print(nikita) # <__main__.Person object at 0x10429ff50>
print(obj1) # Объект от класса A

print(dir(A))
# ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'var1']


print(dir(obj1)) 
# ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'var1', 'var2']

print('hello')
nikita.happy_birthday()


class Calculator:
    def add(self, num1, num2):
        return num1 + num2

    def sqrt(self, num1):
        return num1 ** 0.5

    def percent(self, total_sum, percent_):
        return (total_sum * percent_) / 100
    
    def super_method(self, string):
        res = eval(string)
        return int(res)
        
calc = Calculator()
print(calc.add(5, 5)) # 10
print(calc.sqrt(25)) # 5
print(calc.percent(100, 25)) # 25.0
num1 = calc.super_method('(5-7)**2 - 10')# -6
print(type(num1))
# print(type(calc))
import random

class Sniper:
    health = 100

    def __init__(self, name):
        self.name = name

    def shoot(self, sniper2):
        sniper2.health -= random.randint(1, 20)
        print(f'Атаковал {self}')
        print(f'У {sniper2} осталось {sniper2.health} единиц здоровья')

    def __str__(self) -> str:
        # Когда принтим объект
        return self.name
    
sniper1 = Sniper('nikita')
sniper2 = Sniper('tima')

while sniper1.health > 0 and sniper2.health > 0:
    choice = random.randint(1,2)

    if choice == 1:
        sniper1.shoot(sniper2)
    else:
        sniper2.shoot(sniper1)

if sniper1.health:
    print(f'Победил {sniper1}')
else:
    print(f'Победил {sniper2}')
