import json
import csv
from random import randint
import math
import random
import pandas as pd

def u(): #Задачи 3 (1)
    file = open("example(3.1).txt", "w")
    p=input()
    file.write(p)
    file.close()
    with open("example(3.1).txt", "r") as file:
        data = file.read()
        print(data)
u()


def w4(): #Задачи 3 (2)
    with open("data(3.2).csv") as f:
        a=csv.reader(f)
        for row in a:
            print(row)
w4()

#У меня не хочет погода нормально записываться в файл :( Задача 3(3)

###
All = []

file1 = open("3(4.1).csv", "r")#Задачи 3(4)
data1 = file1.read()
All.append(data1)
file2 = open("3(4.2).csv", "r")
data2 = file2.read()
All.append(data2)
file3 = open("3(4.3).csv", "r")
data3 = file3.read()
All.append(data3)

with open('all(3.4).csv', 'w') as file:
    writer = csv.writer(file)
    for row1 in All:
        writer.writerow(row1)
    file.close()

file1.close()
file2.close()
file3.close()

###

#Задача 3(5)

#Задача 3(6)

###
def Sentence_length(): #Задание 3 (7)
    with open('./3 (7).json', 'r+') as file:
        data = file.read()
        data_json = json.loads(data)
        for i in data_json:
            print(i)
            print('Длина предложения: ')
            print(len(i))

def Keywords():
    with open('./3 (7).json', 'r+') as file:
        data = file.read()
        data_json = json.loads(data)
        for i in data_json:
            if 'локомотивов' in i:
                print(i)

Sentence_length()
Keywords()

###

def sorting(): #Задачи 3(8)
    p = 10
    p1 = []
    for i in range(p):
        p1.append(randint(1, 99))
    print(p1)
    for i in range(p - 1):
        for j in range(p - 1 - i):
            if p1[j] > p1[j + 1]:
                p1[j], p1[j + 1] = p1[j + 1], p1[j]
    print(p1)
sorting()


a=input('Введите любое слово: ') #Задачи 4(1)
count = 0
a1=a
old=[]
new=[]
while True:
    for i in range (len(a)):
        y=random.choice(a)
        old.append(y)
        a=list(a)
        a.remove(y)
        a="".join(a)
    count+=1
    a=a1
    if  "".join(old) not in new:
        new.append("".join(old))
    old=[]
    if len(new) == math.factorial(len(a)) :
        break
print(new)

file = open('4(2).txt','r') #Задачи 4(2)
t=file.readline().split()
t1 = [x for x in t]
new2=[]
for i in range(len(t1)):
   a=t1.count(t1[i])
   new2.append(i)
print(t1[max(new2)], a)

def power(a, n): #задачи 4 (3)
    if n == 0:
        return 1
    elif n == 1:
        return a
    elif n % 2 != 0:
        return a * power(a, n - 1)
    elif n % 2 == 0:
        return power(a * a, n / 2)
a = float(input("Число, которое возводим в степень "))
n = int(input("Число, которое будет являться степенью "))
print(power(a, n))

#Задача 4(4) я не поняла, как это найти:(

old1=[] #задачи 4(5)
with open('4(5).csv') as file:
    reader=csv.reader(file, delimiter=';')
    for row in reader:
       old1.append(row[0])
new=[]
for i in range(len(old1)):
    if old1[i].isdigit():
        new.append(int(old1[i]))
print(sum(new))

#Задача 4(6) вообще не поняла задание:(

file_path = '4(7).csv' #Задача 4(7)
a1 = pd.read_csv(file_path)
s = a1.describe(include='all')
print("Статистика по каждому столбцу:")
print(s)

#Задача 4(8)
#Задача 4(9)
