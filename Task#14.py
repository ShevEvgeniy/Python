# В файле находится N натуральных чисел, записанных через пробел. Среди чисел не хватает одного,
# чтобы выполнялось условие A[i] - 1 = A[i-1]. Найдите это число.
# Пример: 1 2 3 5 6
# Вывод: 4

path = 'C:/Users/shito/Documents/Python/file.txt'
data = open(path, 'r')
string = data.read()
data.close()
list = [int(i) for i in string.split()]
print(list)
for i in range(len(list) - 1):
    if list[i + 1] != list[i] +1:
        print(list[i] +1)