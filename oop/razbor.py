# ООП
"""
ООП - объектно ориентированное программирование, парадигма
1) Наследование
2) Инкапсуляция
3) Полиморфизм

4) Абстракция 
5) Ассоциация
"""

"""
1) Наследование - Принцип ООП, который позволяет одному классу наследовать аттрибуты и методы другого класса
2) Инкапсуляция - Принцип ООП, у которого есть 2 трактовки:
    1) класс является некой капсулой в которой хранятся все аттрибуты и методы
    2) Режимы доступа (Публичный, защищенный, приватный)
3) Полиморфизм - принцип ООП, когда у нас метод называется одинаково, но выполняет разный функционал (Один интерфейс - много реализаций)

4) Абстракция - Принцип ООП, в котором мы создаем класс пустышку от которого наследуются дочерние классы, и переопределяют его методы (Нужен для правильности полиморфизма), абстракция обязует нас переопределять все методы, на которых был декоратор @abstractmethod, если метод не переопределить то выйдет ошибка
5) Ассоциация - Принцип ООП в котором два класса связаны друг с другом, есть два вида связи:
    1) агрегация - слабая
    2) композиция - сильная связь
"""

# class Battery:
#     power = 100

#     def charge(self):
#         if self.power < 100:
#             self.power = 100


# class Iphone:
#     price = 1000
    # category_serializer = CategorySerializer(many=True)


    # def __init__(self, color) -> None:
    #     self.color = color
    #     self.battery = Battery() #КОМПОЗИЦИЯ
    #     self.name = []
    #     self.price = 1000 
    
#     def __init__(self, color, battery: Battery) -> None:
#         self.color = color
#         self.battery = battery # АГРЕГАЦИЯ

# battery1 = Battery()

# iphone = Iphone('black', )
# print(iphone.battery.power)
# del iphone
# print(iphone.battery.power)
# del iphone
# print(battery1)
# print(iphone)

# 1.  Создайте класс Product с атрибутами:
#  • base_price: базовая цена продукта (20000).
#  • model, year, color: аттрибуты экземпляра класса.
#  Реализуйте методы:
#  • has_garanty(year): проверяет гарантию (действует 2 года), возвращает текст о ее состоянии.
#  • change_price(rate): увеличивает base_price на указанный процент.
#  Пример: Создать продукт, повысить цену на 2%, проверить гарантию
# obj.change_price(2)
# print(obj.has_garantiya(2010))
# print(obj.base_price)


class Product:
    base_price = 20000

    def __init__(self, model, year, color) -> None:
        self.model = model
        self.year = year
        self.color = color
    
    def has_garanty(self, current_year):
        past_year = current_year - self.year
        if past_year > 2:
            return 'Гарантия на этот товар истекла'
        return 'Гарантия действительна'

    @classmethod
    def change_price(cls, rate):
        inflation = round(cls.base_price * (rate / 100))
        cls.base_price += inflation

obj1 = Product('A32', 2022, 'white')
print(obj1.change_price(2))
print(obj1.base_price)

# 2. Создайте класс User с атрибутами: (static-class methods)
#  • name, lastname, email.
#  Реализуйте методы:
#  • validate_email(email): проверяет, содержит ли email символ @.
#  • __str__(): возвращает данные пользователя или сообщение о неверном email.
#  • create_user(data): создает пользователя из строки "Имя, Фамилия, email".

# class User:
#     def __init__(self, name, last_name, email) -> None:
#         self.name = name
#         self.last_name = last_name
#         self.email = email

#     @staticmethod
#     def validate_email(email: str) -> bool:
#         return '@' in email and '.' in email[email.index("@"):]
    
#     def __str__(self) -> str:
#         if self.validate_email(self.email):
#             return f"{self.name} - {self.email}"
#         return "Ваш email адрес не валиден"
    
#     @classmethod
#     def create_user(cls, data):
#         user_info = data.split(',') # ['name', 'last_name', 'email']
#         name = user_info[0]
#         last_name = user_info[1]
#         email = user_info[2]
#         user = cls(name, last_name, email)
#         return user
    
# user1 = User.create_user("nikita, grebnev, n@gmail.com")
# print(user1)
# # 3. Создайте класс ADA с атрибутами: (classmethod)
# #  • student_count: количество студентов.
# #  • name, language, kpi: параметры студента.
# #  Реализуйте методы:
# #  • new_student(name, language, kpi): создает нового студента и увеличивает счетчик.
# #  • get_info(): возвращает данные студента.
# #  • set_kpi(kpi): устанавливает новый kpi.
# #  Пример: Создать двух студентов, обновить их kpi, вывести данные и общее число студентов.

# class ADA:
#     student_count = 0

#     def __init__(self, name, language, kpi) -> None:
#         self.name = name
#         self.language = language
#         self.kpi = kpi
    
#     @classmethod
#     def new_student(cls, name, language, kpi):
#         cls.student_count += 1
#         student = cls(name, language, kpi)
#         return student
    
#     def __str__(self):
#         return f"{self.name} - language:{self.language}, kpi: {self.kpi}"
    
#     def set_kpi(self, kpi):
#         self.kpi = kpi
#         return self.kpi
    
# student1 = ADA.new_student('nikita', 'python', 5.0)
# student2 = ADA.new_student('Tima', 'python', 5.0)

# # print(student1.set_kpi(10.0))
# # print(student2.set_kpi(8.0))

# # print(student1)
# # print(student2)
# # print(student1)
# # print(ADA.student_count)

# # 4. Создайте класс Bike с атрибутами:
# #  • cost, make, model, year: себестоимость, производитель, модель, год.
# #  • _sale_price, sold, min_profit: цена продажи, статус продажи, минимальная прибыль.
# #  Реализуйте методы:
# #  • set_cost(): устанавливает цену продажи с учетом минимальной прибыли.
# #  • service(price): увеличивает цену продажи.
# #  • sell(): меняет статус на “продано”, возвращает прибыль.
# #  • get_default_bike(): создает велосипед с параметрами по умолчанию.
# #  Пример: Создать стандартный велосипед, установить себестоимость, добавить обслуживание, продать.


# class Bike:
#     def __init__(self, cost, make, model, year, sale_price, min_profit):
#         self.cost = cost
#         self.make = make
#         self.model = model
#         self.year = year
#         self._sale_price = sale_price
#         self.sold = False
#         self.min_profit = min_profit

#     def set_cost(self):
#         self._sale_price += self.min_profit
#         return self._sale_price

#     def service(self, price):
#         self._sale_price += price
#         return self._sale_price

#     def sell(self):
#         if self.sold:
#             return 'Данный товар уже продан'
#         self.sold = True
#         return f'Прибыль: {self._sale_price - self.cost}'
    
#     @classmethod
#     def get_default_bike(cls):
#         return cls(10000, 'Giant', 'A123', 2024, 20000, 2000)

# bike = Bike.get_default_bike()

# print(bike.set_cost())
# print(bike.service(2000))
# print(bike.sell())


# 5. Создайте класс MoneyFmt с атрибутом:
#  • amount: денежная сумма.
#  Реализуйте методы:
#  • update(amount): обновляет сумму.
#  • __repr__(): возвращает сумму как строку.
#  • dollarize(float_num): форматирует число в денежный вид (например, $1,234.56).
#  • __str__(): возвращает отформатированную сумму.
#  Пример: Создать объект с суммой, обновить ее, проверить формат с отрицательным значением, вывести с помощью repr().

class MoneyFmt:
    def __init__(self, amount) -> None:
        self.amount = amount

    def update(self, amount):
        self.amount = amount

    def __repr__(self) -> str:
        return str(self.amount)

    @staticmethod
    def dollarize(float_num):
        return f'${float_num:,.2f}'.replace("$-", "-$")

    def __str__(self) -> str:
        return MoneyFmt.dollarize(self.amount)

obj1 = MoneyFmt(1400123327689.00)
print(obj1)
obj1.update(-1233892.2143)
print(obj1) # -$1,233,892.21
print(repr(obj1))