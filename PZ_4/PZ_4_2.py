
while True:
    # Обработка исключений
    try:
        N = int(input("Введите первое число "))
        K = int(input("Введите второе число "))
        result = 0
        if N <= K:
            print("Резуьтат равен ", result)
            print("Остаток равен", K)
        else:
            # Цикл с процессом деления
            while not N < K:
                N -= K
                result += 1
            print("Резуьтат равен ", result)
            print("Остаток равен ", N)
    except ValueError:
        print("Ошибка! Введите целые положительные числа")
    except TypeError:
        print("Ошибка! Введите целые положительные числа")
