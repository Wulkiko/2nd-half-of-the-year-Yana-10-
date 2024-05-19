import random
import json
import csv
import math

def alphabet(): #Задачи 1(1)
        s = input()
        print(*sorted(list(s.split())))
alphabet()

def the_sum_of_the_primes(n): #Задачи 1(2)
        for i in range(2, n // 2 + 1):
                if (n % i == 0):
                        return (0)
        return (1)
a = int(input("Вверхняя грань: "))
b = int(input("Нижняя грань: "))
a1 = []
b1 = 0
for i in range(a, b + 1):
        if (the_sum_of_the_primes(i)):
                a1.append(i)
print('Сумма всех простых чисел: ', sum(a1))

def palindrome():
        s = input()  # задачи 1 (3)
        s1 = s.lower()
        s2 = s1[::-1]
        print(s2)
        if s2 == s1:
                print('Это слово палиндром')
        else:
                print('Это не палиндром')
palindrome()


def rock_paper_scissors():
        p = 0  # задачи 1 (4)
        while (p == 0):
                a = int(input("1 - камень, 2 - ножницы, 3 - бумага. "))
                if (a == 1 or a == 2 or a == 3):
                        p = 1
        b = random.randint(1, 3)
        if b == 1:
                print("Программа выбрала  камень.")
        if b == 2:
                print("Программа выбрала ножницы.")
        if b == 3:
                print("Программа выбрала бумагу.")

        if a == b:
                coute = 0
        if a == 1 and b == 2:
                coute = 1
        if a == 1 and b == 3:
                coute = 2
        if a == 2 and b == 1:
                coute = 2
        if a == 2 and b == 3:
                coute = 1
        if a == 3 and b == 1:
                coute = 1
        if a == 3 and b == 2:
                coute = 2
        if coute == 0:
                print("Ничья")
        if coute == 1:
                print("Победили вы")
        if coute == 2:
                print("Победил программа")
rock_paper_scissors()

#Я не понимаю как это сделать :( Задачи 1(5)

class Book: #Задание 2(1)

        def __init__(self, title, author):
                self.title = title
                self.author = author

        def get_title(self):
                return 'Название: ' + self.title

        def get_author(self):
                return 'Автор: ' + self.author


Book1 = Book('«История Предприятия 3826»', 'Харальд Хорф')
print(Book1.title)


class Soda: #Задачи 2 (2)
        def __init__(self, value=None):
                self.value = value
        def show_my_drink(self):
                q = self.value
                if q:
                        print(f'Газировка и {self.value}')
                else:
                        print('Обычная газировка')
Soda1 = Soda('Клубника')
Soda1.show_my_drink()


class TriangleChecker: #задачи 2 (3)
        def __init__(self, a=0, b=0, c=0):
                self.a = a
                self.b = b
                self.c = c

        def is_triangle(self):
                if self.a and self.b and self.c <0:
                        raise ValueError('С отрицательными числами ничего не выйдет!')
                if not isinstance((self.a and self.b and self.c),int):
                        raise TypeError('Нужно вводить только числа!')
                if (self.a and self.b and self.c)<3:
                        raise ValueError('Жаль, но из этого треугольник не сделать')
                else:
                        return 'Ура, можно построить треугольник!'

triangale1 = TriangleChecker(3, 7, 5)
print(triangale1.is_triangle())

class Nikola: #Задачи 2 (4)
        __slots__ = ['name', 'age']

        def __init__(self, name, age):
                if name == 'Николай':
                        self.name = name
                else:
                        self.name = f'Я не {name}, а Николай'
                        self.age = age
Nikola1=Nikola('dk', 12)
print(Nikola1.name)

class Biblioteka: #Задачи 2 (5)
        def __init__(self, list_of_books):
                self.list_of_books = list_of_books
        def add_a_book(self, book):
                self.list_of_books.append(book)
        def delete_a_book(self, book):
                self.list_of_books.remove(book)
        def search(self, book):
                a = input('введите книгу, которую Вам нужно найти: ')
                for i in self.list_of_books:
                        if i == a:
                                print('эта книга есть в списке: ', self.list_of_books)
                        else:
                                print('Этой книги нет')
                        break
Biblioteka1 = Biblioteka(['Ворота Расемон', 'Виишневый сад', 'Коттедж'])
Biblioteka1.search("Ворота Расемон")


class Aviakompania: #Задачи 2(6)
        def __init__(self, planes, route):
                self.planes = planes
                self.route = route
        def append_airplane_model(self, airplane_model):
                self.planes.append(airplane_model)
                print('вы добавили модель:', airplane_model)
                print('новый список самолётов:', self.planes)
        def remove_airplane_model(self, airplane_model):
                self.planes.remove(airplane_model)
                print('вы удалили данную модель:', airplane_model)
                print('новый список самолётов:', self.planes)
        def append_route(self, city):
                self.route.append(city)
                print('вы добавили город в маршрут:', city)
                print('новый список маршрутов:', self.route)
        def remove_route(self, city):
                self.route.remove(city)
                print('вы удалили данный город:', city)
                print('новый список маршрутов:', self.route)
        def search(self):
                s = [0]
                a = input('введите модель, которую надо найти: ')
                for i in self.planes:
                        if i == a:
                                print('модель есть в списке самолётов: ', self.planes)
                                s.append(1)
                        else:
                                s.append(0)
                d = sum(s)
                if d == 0:
                        print('Такой модели нет')
        def search2(self):
                u = [0]
                j = input('введите город, который надо найти: ')
                for i in self.route:
                        if i == j:
                                print('город есть маршруте: ', self.route)
                                u.append(1)
                        else:
                                u.append(0)
                d = sum(u)
                if d == 0:
                        print('такого города нет')
Aviakompania1 = Aviakompania(['Boeing 767-200', 'Airbus A321neo'], ['Новосибирск', 'Токио'])
Aviakompania1.append_airplane_model('sdvf')

class Bank: #Задачи 2 (7)
        def __init__(self, owner, account_number, balance):
                self.owner = owner
                self.account_number = account_number
                self.balance = balance
        def top_up_your_account(self):
                a = int(input('введите сумму для ввода:  '))
                a1 = a * 0.99
                a2 = self.balance + a1
                print('на вашем балансе: ', a2)

        def withdraw_from_the_account(self):
                b = int(input('введите сумму для вывода: '))
                b1 = b * 1.01
                if self.balance < b1:
                        print('на вашем счету недостаточно средств.')
                else:
                        b2 = self.balance - b1
                        print('на вашем балансе: ', b2)
                        print('вы сняли: ', b)
        def show_balanse(self):
                print('на вашем балансе: ' + self.balance)
Bank1 = Bank("Никита", '2500', 1300)
Bank1.top_up_your_account()

class Point: #Задачи 2(8)
        def __init__(self, x1, y1, x2, y2):
                self.x2 = x2
                self.y2 = y2
                self.x1 = x1
                self.y1 = y1
        def distance(self):
                a = math.sqrt((self.x2 - self.x1) ** 2 + (self.y2 - self.y1) ** 2)
                print("расстояние между точками -", a)
        def the_axis(self):
                if self.x1 == 0:
                        print('точка 1 лежит на оси OY')
                if self.x2 == 0:
                        print('точка 2 лежит на оси OY')
                if self.y1 == 0:
                        print('точка 1 лежит на оси OX')
                if self.y2 == 0:
                        print('точка 2 лежит на оси OX')
point1 = Point(6, 4, 4, 0)
point1.distance()


class product: #Задачи 2(9)
        def __init__(self, title, price, quantity):
                self.title = title
                self.price = price
                self.quantity = quantity
        def increasing_the_number_of(self):
                print('Товара "', self.title, '" -', self.quantity)
                a = int(input('На сколько увеличить количества товара: '))
                a1 = self.quantity + a
                print('на складе теперь ', a1, " товарa")
        def reducing_the_number_of(self):
                print('Товара "', self.title, '" -', self.quantity)
                b = int(input('Hа сколько уменьшить количества товара:  '))
                b1 = self.quantity - b
                if b > self.quantity:
                        print('на складе мало товара')
                else:
                        print('на складе теперь ', b1, " товара")
        def cost(self):
                print('На складе  товара "', self.title, '" -', self.quantity)
                с = self.quantity * self.price
                print('Общая стоимость всего товара: ', с)


product1 = product("Кокос", 200, 290)
product1.increasing_the_number_of()


class Student: #Задачи 2(10)
        def __init__(self, name, age, list, evaluations):
                self.list = list
                self.name = name
                self.age = age
                self.evaluations = evaluations
        def add_a_rating(self, list):
                self.list.append(list)
                print(self.list)
                s = int(input('оценку по новому предмету: '))
                if s > 5 or s < 2:
                        print('оценка может быть от 2 до 5')
                else:
                        self.evaluations.append(s)
                        print('все оценки по предметам: ', self.evaluations)
        def delete_an_item(self, Lesson):
                for i in range(len(self.list)):
                        if self.list[i] == Lesson:
                                self.evaluations.remove(self.evaluations[i])
                self.list.remove(Lesson)
                print(self.list)
                print(self.evaluations)
        def average_score(self):
                print('все предметы ученика:', self.list)
                s = sum(self.evaluations)
                w = s / len(self.evaluations)
                print('средний балл студента:', w)
Student1 = Student('Никель', 21, ['философия', 'обж', 'право', 'физ-ра'], [5, 4, 3, 2])
Student1.average_score()
