# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл (или вывести в терминал) многочлен степени k.

# Пример:

# - k = 2  => 2*x² + 4*x + 5
# - k = 3  => 41*x^3 + 6*x² + 2*x + 98

from random import randint
import random

k = int(input('Введите число k: '))

result = ''
temp = []
for i in range(k):
    temp.append(randint(0, 100))


znak = ['+', '-']
i = 0
j = 0
while k > 1:
    if temp[i] != 0:
        result += (f'{temp[i]}x**{k}{random.choice(znak)}')
    k -= 1
    i += 1


if temp[-1] != 0:
    result += (f'{temp[-1]}=0')
else:
    result += ('=0')
# with open('result.txt', 'w', encoding='utf8') as file:
#     file.write(f'Сгенерированные числа: {temp}\nОтвет: {result}')
print(f'Сгенерированные числа: {temp}\nОтвет: {result}')