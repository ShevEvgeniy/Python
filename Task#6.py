# Напишите программу, в которой пользователь будет задавать две строки, одна из них - буква, а вторая фраза/слово,
# программа должна посчитать сколько раз буква встретилась буква во второй строке (не используя встроенные функции)

string_to_search = input('Введите строку. \n').lower()
char_to_find = input('Введите букву, которую хотите найти и посчитать количество вхождений. \n').lower()
counter = 0
for char in string_to_search:
    if char == char_to_find:
        counter += 1
print(f'В данной строке символ "{char_to_find}" встречается {counter} раз(а)')