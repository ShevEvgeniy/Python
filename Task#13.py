# Задайте два числа. Напишите программу, которая найдет НОК (наименьшее общее кратное) этих двух чисел.

a = int(input('a = '))
b = int(input('b = '))
nod = 1
for i in range(2, (min(a,b)) + 1):
    if a % i == 0 and b % i == 0:
        nod = i
nok = a*b/nod
print(nok)