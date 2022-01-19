f1 = open("1.txt", 'w')
f1.write("24 -48 13 32 -16")
f1 = open('1.txt', 'r')
numbers = f1.read()
numbers = numbers.split()
print(f1.read())


def d3():
    x = 0
    for i in range(len(numbers)):
        if int(numbers[int(i)]) % 3 == 0:
            print("Числа, кратные 3: ", numbers[int(i)])
    for d in range(len(numbers) - 1):
        x += int(numbers[int(d)]) * int(numbers[int(d + 1)])
    print("Произведение эл-ов: ", x)
    print(min(numbers))


d3()
