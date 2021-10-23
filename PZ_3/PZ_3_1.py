while True:
    # Обработка исключений
    try:
        while True:
            # Проверка условия
            x = int(input("Введите четырёхзначное число "))
            if x >= 10000:
                print("Слишком большое число")
                continue
            if x <= 999:
                print("Слишком маленькое число")
                continue
            break
        first = x // 1000
        second = x // 100 % 10
        third = x // 10 % 10
        forth = x % 10
        if str(forth) + str(third) + str(second) + str(first) == str(first) + str(second) + str(third) + str(forth):
            print("Истина")
            break
        else:
            print("Ложь")
            break
    except ValueError:
        print("Ошибка! Введите четырёхзначное число")
    except TypeError:
        print("Ошибка! Введите четырёхзначное число")
