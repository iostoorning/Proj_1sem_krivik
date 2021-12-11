# Дана строка 'груши 45 991 63 100 12 яблоки 13 47 26 0 16'
# Преобразовать информацию из строки в словари
# С использованием функции найти минимальные продажи по каждому виду продукции
# Вывести результаты
x = "груши 45 991 63 100 12 яблоки 13 47 26 0 1"
print(x)
x = x.split()
pears = {1: x[1], 2: x[2], 3: x[3], 4: x[4], 5: x[5]}
apples = {1: x[7], 2: x[8], 3: x[9], 4: x[10], 5: x[11]}
minpears = 0
minapples = 0

def min_sales() :
    i = 1
    for i in pears:
        y = pears[i]
        if y <= pears[i]:
            continue
        else:
            y = pears[i]
        i += 1
        y = minpears
        return i
    for i in apples:
        y = apples[i]
        if y <= apples[i]:
            continue
        else:
            y = apples[i]
        i += 1
        y = minapples
        return i
    print('Минимальные продажи груш = ', minpears)
    print('Минимальные продажи яблок = ', minapples)


min_sales()
