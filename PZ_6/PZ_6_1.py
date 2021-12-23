# Дан список ненулевых целых чисел размера N. Проверить, образуют ли его элементы
# геометрическую прогрессию. Если образуют, то вывести знаменатель прогрессии, если
# нет — вывести 0.
while True:
    try:
        x = input("Введите список чисел через запятую без пробела: ")
        x.split()
        NList = list(x)
        y = float(NList[2]) / float(NList[0])
        for i in range(len(NList) - 1):
            if y == float(NList[i + 2]) / float(NList[2]):
                continue
            else:
                y = 0
                break
        print(y)
        break
    except TypeError:
        print("Ошибка значения! Вводите числа")
    except ValueError:
        print("Ошибка значения! Вводите числа")
