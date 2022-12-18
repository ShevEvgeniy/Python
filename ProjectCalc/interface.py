import digit, in_num, log

def button_click():
    print('введите "0" если хотите продолжить')
    print('введите "1" если хотите закончить')
    flag = int(input())
    while flag == 0:
        primer = digit.parse() # [1, "+" 3, "*", 2]
        result = digit.calculate(primer)
        in_num.view_data(result)
        log.loger(primer, result)
        print('Введите "0" если хотите продолжить')
        print('Введите "1" если хотите закончить')
        flag = int(input())
    print("Программа завершилась, Удачи!")