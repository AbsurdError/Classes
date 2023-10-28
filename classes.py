# class Person:
#     kind = 'men'
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def say(self, message):
#         print(message)
#
#     def say_hello(self):
#         self.say(f'Hello. My name is {self.name}. \nI\'m {self.age} years old.')
#
#     def __del__(self):
#         print('Объект уничтожен', self.name)
#
# tom = Person('Tom', 15)
# bob = Person('Bob', 16)
#
#
# # print(tom.age, tom.kind)
# # print(bob.kind)
# # print(bob.name)
# # print(tom.name)
# # tom.say_hello()
# # bob.say_hello()
# # bob.age = 26
# # bob.say_hello()
# # print(bob.age)
# # str = '1 2 3 4'
# # s = str.split()
# # print(len(s))
#
#
# tom.height = 1.80
# bob.weight = 50
# print(f'Рост Тома {tom.height} м')
# print(f'Вес Боба {bob.weight} кг')
#
# del bob
# jim = Person('Jim', 18)
# print(tom.name)
# print(jim.name)

# class Point3D:
#     def __init__(self, x = 0, y = 0, z = 0):
#         self.x = x
#         self.y = y
#         self.z = z
#
#     def info(self):
#         print(f'x = {self.x}, y = {self.y}, z = {self.z}')
#
#     def distance(self, a, b):
#         return b - a
#     def distance2(self):
#         return f'Расстояние от х до у: {self.distance(self.x, self.y)}. \nРасстояние от y до z: {self.distance(self.y, self.z)}. \nРасстояние от х до z: {self.distance(self.x, self.z)} '
#
#
# first = Point3D(4, 5, 8)
# second = Point3D(5, 8, 7)
# third = Point3D(8, 7, 3)
# print(first.x)
# print(first.distance2())


# class Square:
#     def __init__(self, a):
#         self.a = a
#     def square_a(selfs, a):
#         return a**2
#     def perimeter(self, a):
#         return a * 4
#     def result(self):
#         return f'Площадь квадрата со стороной {self.a} = {self.square_a(self.a)} \nПериметр квадрата со стороной {self.a} = {self.perimeter(self.a)}'
# one = Square(7)
#
# print(one.result())

# import math
# class Triangle:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#     def square_ab(self, a, b):
#         return 0.5 * a * b
#     def perimeter(self, a, b):
#         c = math.sqrt(self.a ** 2 + self.b ** 2)
#         return self.a + self.b + c
#     def result(self):
#         return f'Площадь треугольника с катетами а = {self.a} и b = {self.b} равна: {self.square_ab(self.a, self.b)} \nПериметр треугольника с катетами а = {self.a} и b = {self.b} равна: {self.perimeter(self.a, self.b)}'
#
# one = Triangle(3, 5)
# print(one.result())


# import math
#
# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def distance_to(self, other_point):
#         distance = math.sqrt((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2)
#         return distance
#
# class Triangle:
#     def __init__(self, A, B, C):
#         self.A = A
#         self.B = B
#         self.C = C
#
#     def perimeter(self):
#         # Вычисляем периметр треугольника, сложив длины всех его сторон
#         side1 = self.A.distance_to(self.B)
#         side2 = self.B.distance_to(self.C)
#         side3 = self.C.distance_to(self.A)
#         perimeter = side1 + side2 + side3
#         return perimeter
#
# point_A = Point(2, 4)
# point_B = Point(6, 9)
# point_C = Point(6, 0)
# triangle = Triangle(point_A, point_B, point_C)
# print(f"Периметр треугольника: {triangle.perimeter()}")

# class CPerson:
#     def __init__(self, first_name="", last_name="", middle_name="", day=1, month=1, year=2000, gender=""):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.middle_name = middle_name
#         self.day = day
#         self.month = month
#         self.year = year
#         self.gender = gender
#
#     def set_info(self, first_name, last_name, middle_name, day, month, year, gender):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.middle_name = middle_name
#         self.day = day
#         self.month = month
#         self.year = year
#         self.gender = gender
#
#     def get_info(self):
#         return f"Ф.И.О.: {self.last_name} {self.first_name} {self.middle_name}\nДата рождения: {self.day}.{self.month}.{self.year}\nПол: {self.gender}"
#
#     def __del__(self):
#         print(f"Объект {self.first_name} {self.last_name} удален")
#
# person = CPerson()
# person.set_info("Даниель", "Литао", "Романович", 10, 7, 2006, "Мужской")
# print(person.get_info())

# class Phone:
#     def __init__(self, number, model, weight):
#         self.number = number
#         self.model = model
#         self.weight = weight
#
#     def receiveCall(self, name):
#         print(f"Звонит {name}")
#
#     def getNumber(self):
#         return self.number
#
# phone2 = Phone("987-654-3210", "Samsung Galaxy A21", 120)
# phone2.receiveCall("Петр")
# print(f'Телефон:\nМодель: {phone2.model} \nНомер: +7 {phone2.number} \nВес: {phone2.weight}')


# class Reader:
#     def __init__(self, full_name, library_card_number, faculty, birthdate, phone):
#         self.full_name = full_name
#         self.library_card_number = library_card_number
#         self.faculty = faculty
#         self.birthdate = birthdate
#         self.phone = phone
#     def information_about_the_reader(self):
#         return f'Ф.И.О: {self.full_name} \nНомер читательского билета: {self.library_card_number} \nФакультет: {self.faculty} \nДата рождения: {self.birthdate} \nТелефон: {self.phone}'
#     def takeBook(self, num_books):
#         print(f"{self.full_name} взял {num_books} книги")
#
#     def returnBook(self, num_books):
#         print(f"{self.full_name} вернул {num_books} книги")
#
# # Пример использования класса Reader:
# reader1 = Reader("Смирнов В. В.", "12345", "Архитектура", "11.05.2004", "8 123-456-7890")
# reader1.takeBook(3)
# reader1.returnBook(3)
# print(reader1.information_about_the_reader())