# Напишите программу, удаляющую из текста все слова, содержащие "абв". Строка находятся в файле.
# Пример: ывпвап вапапро приветабв привет приветаб
# Вывод: ывпвап вапапро привет приветаб

path = 'C:/Users/shito/Documents/Python/new.txt'
data = open(path, 'r', encoding='UTF-8')
string = data.read()
data.close()
list0 = string.split()
print(list0)
list1 = list(filter(lambda x: not 'абв' in x, list0 ))
print(list1)