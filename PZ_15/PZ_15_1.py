# В матрице найти отрицательные элементы, сформировать из них новый массив.
# Вывести размер полученного массива
import random as rnd
import numpy as np

arr1 = np.matrix([[rnd.randrange(-2, 5), rnd.randrange(-2, 5)],
                  [rnd.randrange(-2, 5), rnd.randrange(-2, 5)]])
result = []
for n in range(2):
    for i in range(2):
        if arr1[[n][i]] < 0:
            result = [result.append(arr1[[n][i]])]

print(result)
