# Дана последовательность чисел. Получить список уникальных элементов заданной последовательности. Без использования Count()
# *Пример*
# [1, 2, 3, 5, 3, 10] => [2, 10]

# from random import randrange

# quantity = 10
# list1 = [randrange(7) for i in range(quantity)]
# print('Список из случайных чисел:', *list1)

# list2 = []
# for k in list1:
#     b = 0
#     for g in list1:
#         if k == g:
#             b += 1
#     if b == 1:
#         list2.append(k)
# print('Уникальные элементы списка:', *list2)


def find_unigue(data):
    result = []
    results_new = []
    for el in data:
        if el not in result and el not in results_new:
            result.append(el)
            results_new.append(el)
        elif el in result:
            result.remove(el)
    print(results_new)
    return sorted(result)

sequence = [1, 1, 2, 2, 3, 10]
print(f'Исходная последовательность: {sequence}')
print(f'Отсортированный список уникальных элементов: {find_unigue(sequence)}')


