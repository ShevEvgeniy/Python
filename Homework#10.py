# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

spisok = input('Введите элементы через пробел\n').split()
list = []
i = 0
while (i < len(spisok)//2 + len(spisok)%2):
    numb = len(spisok) - i - 1
    list.append(int(spisok[i]) * int(spisok[numb]))
    i+=1

print(list)