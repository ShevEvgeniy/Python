# Напишите программу которая принимает на вход два числа
# и проверяет, явлеяется ли одно число квадратом другого.

num1 = int(input("Введите первое число\n"))
num2 = int(input("Введите второе число\n"))

if num1 == num2 ** 2 or num2 == num1 ** 2:
    print("Да, одно из чисел является квадратом другого")
else:
    print("Нет, ни одного из чисел не является квадратом другого")
