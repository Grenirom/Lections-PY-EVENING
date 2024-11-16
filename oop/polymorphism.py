"""
Полиморфизм - принцип ООП, в котором в разных классах методы называются одинаково, но реализация разная

"Один интерфейс - много реализаций"
"""


class Dog:
    def speak(self):
        print('Гав')


class Cat:
    def speak(self):
        print('Мяу')


class Frog:
    def speak(self):
        print('Ква')

objects = [Frog(), Cat(), Dog()]

for obj in objects:
    obj.speak()
    

# __add__ (+) - метод полиморф
print(5 + 5)
print('hello' + 'hello')
print('5' + '5')
print([1,2,3,4] + [5,6,7])
a = [1, 2, 4, 5]
b = [4, 4, 4]
print(a.__add__(b))

# функция полиморф -> len(): __len__
print(len('hello'))
print(len([1, 2, 3]))
print(len({1: 1, 2: 2}))
print('abc'.__len__())

from math import pi


class Shape:
    def __init__(self, name) -> None:
        self.name = name

    def area(self):
        pass

    def fact(self):
        return f'Я фигура в двумерной плоскости: {self.name}'
    


class Sqare(Shape):
    def __init__(self, length) -> None:
        super().__init__('Квадрат')
        self.length = length

    def area(self):
        return self.length ** 2
    
    def fact(self):
        return super().fact() + '\nУ квадрата все стороны равны и углы равны 90 градусам!'
       
    
class Circle(Shape):
    def __init__(self, radius) -> None:
        super().__init__('Окружность')
        self.radius = radius

    def area(self):
        return pi * (self.radius ** 2)
    

obj1 = Sqare(8)
obj2 = Circle(3)

print(obj1.area())
print(obj1.fact())
print()
print(obj2.area())
print(obj2.fact())
