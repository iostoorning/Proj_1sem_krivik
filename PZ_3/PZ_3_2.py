while True:
    # Обработка исключений
    try:
        while True:
            x = int(input("Введите первый координат первого поля "))
            y = int(input("Введите второй координат первого поля "))
            xx = int(input("Введите первый координат второго поля "))
            yy = int(input("Введите первый координат второго поля "))
            # Проверка условия
            if x >= 9 or x <= 0:
                print("Введите числа от 1 до 8")
                continue
            elif y >= 9 or y <= 0:
                print("Введите числа от 1 до 8")
                continue
            elif xx >= 9 or xx <= 0:
                print("Введите числа от 1 до 8")
                continue
            elif yy >= 9 or yy <= 0:
                print("Введите числа от 1 до 8")
                continue
            break
        # Выполнение задачи и вывод результата
        if x == xx or y == yy:
            print("Истина")
            break
        else:
            print("Ложь")
            break
    except ValueError:
        print("Ошибка! Введите числа от 1 до 8")
    except TypeError:
        print("Ошибка! Введите числа от 1 до 8")
