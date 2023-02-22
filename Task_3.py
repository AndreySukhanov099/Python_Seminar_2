#Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

while True:
    n =int(input("Введите число N > 1 "))
    if n >1:
        break
b =[]
for i in range(1,n):
    if i%2 == 0:
        b.append(i)
print(b)