# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.(Вывод тех элементов, которые были без повторов)

# Ввод: 1 2 3 2 4 4
# Вывод: 1 3

n = list("123244")

list = n
print("Ввод:", list)

list_count = []
for i in list:
    count = 0
    for k in list:
        if k == i:
            count += 1
    list_count.append(count)
print(list_count)

result = []
for i in range(len(list_count)):
    if list_count[i] == 1:
        result.append(list[i])
print("Вывод:", result)