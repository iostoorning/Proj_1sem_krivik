while True:
    try:
        A = int(input("Введите целое число "))
        B = int(input("Введите целое число, болшее прошлого "))
        if A >= B:
            print("Ошибка! Второе число больше или равно первому")
            continue
        else:
            t = B - A
            while t != 0:

                t -= 1
        break
    except ValueError:
        print("Ошибка значения! Вводите целые числа")
