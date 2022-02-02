# Дано множество A из N точек (точки заданы своими координатами x, у). Найти пару
# различных точек этого множества с максимальным расстоянием между ними и само это
# расстояние (точки выводятся в том же порядке, в котором они перечислены при
# задании множества A).
import math

while True:
    try:
        points = str(input("Введите координаты точек через двоеточие, разделяя запятой: "))
        A = set(points.split(","))
        N = len(A)
        listA = list(A)
        listx = []
        listy = []
        Rmax = 0
        maxpoint1 = 0
        maxpoint2 = 0
        for i in range(N):
            point = str(listA[i]).split(":")
            x = point[0]
            y = point[1]
            listx.append(x)
            listy.append(y)
        for i in range(N - 1):
            x1 = listx[i]
            x2 = listx[i + 1]
            y1 = listy[i]
            y2 = listy[i + 1]
            x3 = float(x2)-float(x1)
            y3 = float(y2)-float(y1)
            R = math.sqrt(x3 ** 2 + y3 ** 2)
            if R >= Rmax:
                R = Rmax
                maxpoint1 = listA[i]
                maxpoint2 = listA[i + 1]
        print("Максимальное расстояние = ", Rmax)
        print("Точки с максимальным расстоянием: ", maxpoint1, ", ", maxpoint2)
        break
    except TypeError:
        print("Ошибка типов! Введите численные координаты точек через двоеточие, разделяя запятой")
    except ValueError:
        print("Ошибка значения! Введите численные координаты точек через двоеточие, разделяя запятой")
