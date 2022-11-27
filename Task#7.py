# Петя и Катя - брат и сестра. Петя - студент, а Катя - школьница. Петя помогает Кате по математике.
# Он задумывает два натуральных числа, а Катя должна их отгадать
# Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P 
# Помогите Кате отгадать задуманные Петей числа.
# Пример
# Ввод: 4 4
# Вывод: 2 2
# Пример
# Ввод: 5 6
# Вывод: 2 3

# petya_chislo_1 = int(input('введите сумму. \n'))
# petya_chislo_2 = int(input('введите произведение. \n'))

# for x in range(1,petya_chislo_1):
#     for y in range(1,petya_chislo_1):
#         if ((x * y) == petya_chislo_2) and ((x + y) == petya_chislo_1):
#             print(f'Петя сказал, что сумма загаданных чисел это {petya_chislo_1}, а их произведение это {petya_chislo_2}.')
#             print(f'Катя ответила: "Так это же {x} и {y}".')
#             break

# a = int(input('введите сумму: '))
# b = int(input('Введите произведение: '))
# res = []
# for i in range(a * b):
#     if i == (a * i - b)**0.5:
#         res.append(i)
# print(*res if len(res) == 2 else res + res)

vvod = input().split()
s = int(vvod[0])
p = int(vvod[1])
for i in range(s+1):
    if (i * (s-i) == p):
       print(i, s-i)
       break
