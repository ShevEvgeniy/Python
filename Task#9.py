# Напишите программу, которая определит позицию второго вхождения строки в списке либо сообщит, что её нет.

# список: ['qwe', 'asd', 'zxc', 'qwe', 'ertqwe'], ищем: 'qwe', ответ: 3
# список: ['йцу', 'asd', 'ячс', 'цук', 'йцукен'], ищем: 'йцу', ответ: 5
# список: ['йцу', 'фыв', 'ячс', 'цук', 'йцукен'], ищем: 'йцу', ответ: -1
# список: ['123', '234', '123', '567'], ищем: '123', ответ: -1
# список: [] ищем: '123', ответ: -1

# list = ['qwe', 'asd', 'zxc', 'qwe', 'ertqwe']
# list = ['йцу', 'asd', 'ячс', 'цук', 'йцукен']
# list = ['йцу', 'фыв', 'ячс', 'цук', 'йцукен']
list = ['123', '234', '123', '567']
# list = []

second_entry = input()
counter = 0
for i in range(len(list)):
    if list[i] == second_entry and counter == 1:
        print(i)
        break
    if list[i] == second_entry and counter == 0:
        counter +=1
else:
    print("-1")