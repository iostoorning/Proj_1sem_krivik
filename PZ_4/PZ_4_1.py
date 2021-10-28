while True:
    # Обработка искючений
    try:
        A = int(input("Введите целое число "))
        B = int(input("Введите целое число, болшее прошлого "))
        # Проверка условия
        if A >= B:
            print("Ошибка! Второе число больше или равно первому")
            continue
        else:
            t = B - A
            n = 1
            i = 0
            while t != -1:
                i += 1
                while n != 0:
                    print(A)
                    n -= 1
                A += 1
                t -= 1
                n = + 1 + i
        break
    except ValueError:
        print("Ошибка значения! Вводите целые числа")
    except TypeError:
        print('Ошибка ввода! Введитте целые числа')
