# Напишите программу, которая на вход принимает 5 чисел
# ми находит максимальное из них

INDEX = 5
nums = []
for num in range(INDEX):
    nums.append(int(input('Введите число: \n')))
print(f'max = {max(nums)}')
