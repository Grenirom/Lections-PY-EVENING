"""
Ассоциация - принцип ООП, в котором два класса связаны друг с другом. Связь обозначает то, что внутри одного объекта будет существовать другой объект от другого класса

ВИДЫ СВЯЗЕЙ:
Агрегация - слабая связь
Композиция - сильная связь
"""


# Пример с сильной связью (Композиция)


class Battery:
    power = 100

    def charge(self):
        if self.power < 100:
            self.power = 100


class Iphone:
    def __init__(self, color) -> None:
        self.color = color
        self.battery = Battery()
        # Когда мы создаем внутри класса объект от другого класса, это - Композиция (сильная связь)

# print(a) NameError
# При удалении объекта от класса Iphone, вместе с ним удаляется и батарейка


# Пример со слабой связью - Агрегация


class Nokia:
    def __init__(self, battery, color):
        self.color = color
        self.battery = battery
        # Когда объект создается из вне класса и передается внутрь, это - Агрегация

    def __str__(self) -> str:
        return 'nokia'
    
battery = Battery()
nokia1 = Nokia(battery, 3)
print(nokia1.color)
print(nokia1.battery.power)
nokia1.battery.power -= 50
print(nokia1.battery.power)
nokia1.battery.charge()
print(nokia1.battery.power)
del nokia1
# print(nokia1)
print(battery.power)
nokia2 = Nokia(battery, 'Blue')
print(nokia2)
print(nokia2.battery.power)

# Пример с композицией

class Wall:
    def __init__(self, direction) -> None:
        self.type = direction

    def __str__(self) -> str:
        return f'{self.type}'

class Room:
    def __init__(self) -> None:
        self.west_wall = Wall('west')
        self.east_wall = Wall('east')
        self.south_wall = Wall('south')
        self.north_wall = Wall('north')

obj = Room()
print(obj.west_wall)
print(obj.east_wall)
print(obj.north_wall)

# Композиция


class Engine:
    country = 'Germany'

    def __init__(self, power, type) -> None:
        self.power = power
        self.type = type

    def __str__(self) -> str:
        return f'Power: {self.power}'
    

class Audi:
    brand = 'Audi'
    country = 'Germany'

    def __init__(self, model, power, engine_type) -> None:
        self.engine = Engine(power, engine_type)
        self.model = model

    def __str__(self) -> str:
        return f'{self.brand} {self.model} -> Engine: {self.engine.type} -> engine country: {self.engine.country}'
    

car = Audi(model='RS6', power=500, engine_type='V8')
print(car)
