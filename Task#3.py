# Напишите программу, которая будет принимать число N и выводить числа от -N до Т
num = int(input("Введите число N\n"))
if num > 0:
    print([i for i in range(-num, num + 1)])
else:
    print([i for i in range(num, -num + 1)])
