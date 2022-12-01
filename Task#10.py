# Реализуйте алгоритм задания случайных чисел без использования встречного генератора псевдослучайных чисел

def GetRandomNumber() -> int:
    userinp = input("Введите границы числового диапазона через пробел.\n").split()
    minimum = int(userinp[0])
    maximum = int(userinp[1])
    userinp = input("Ткните пальцем в небо (в клавиатуру).\n")
    rnum = [ord(x) for x in userinp]
    rnum = sum(rnum)
    res = rnum
    while res > maximum:
        res -= minimum
    return res

print(GetRandomNumber())