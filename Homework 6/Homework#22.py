# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# Пример:
# - 6782 -> 23
# - 0,56 -> 11

# def summa(num):
#     return sum(map(int, num.replace('.', '').replace('-', '')))

# num = input('Введите число: ')
# print(f'Сумма цифр в числе: {summa(num)}')





n = input('Введите число: ')
sum = sum(map(int, n.replace('.', '').replace('-','')))
print (sum)
