while True:
    try:

        def RectPS(x, xx, y, yy, P, S):
            if 0 < xx > x < 0:
                P = 2 * (xx + x) + 2 * (yy + y)
                S = (xx + x) * (yy + y)
            elif 0 < x > xx < 0:
                P = 2 * (x + xx) + 2 * (y + yy)
                S = (x + xx) * (y + yy)
            elif xx > x:
                P = 2 * (xx - x) + 2 * (yy - y)
                S = (xx - x) * (yy - y)
            elif x > xx:
                P = 2 * (x - xx) + 2 * (y - yy)
                S = (x - xx) * (y - yy)
            elif P < 0:
                P *= -1
            elif S < 0:
                S *= -1
            S = round(S)
            P = round(P)
            print("Площадь равна = ", S, "Периметр равен = ", P)


        x1 = float(input("Введите первую координату первой стороны "))
        x2 = float(input("Введите вторую координату первой стороны "))
        y1 = float(input("Введите первую координату второй стороны "))
        y2 = float(input("Введите вторую координату второй стороны "))
        RectPS(x1, x2, y1, y2, P=0, S=0)
        break
    except ValueError:
        print("Ошибка! Вводите числа")
