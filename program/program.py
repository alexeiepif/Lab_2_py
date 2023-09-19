import numpy as nmp
print("hello ivt")
print("it is my program")
print("Таблица умножения")
a = []
for i in range(1,11):
    b = []
    for j in range(1,11):
        b.append(i*j)
    a.append(b)
print(nmp.matrix(a))
print("Работу выполнил Епифанов А.А.")