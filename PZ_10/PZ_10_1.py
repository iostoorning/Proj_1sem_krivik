f1 = open("1.txt")
f1.write("24 -48 13 32 -16")
numbers = f1.read()
numbers = numbers.split()
print(f1.read())


def d3():
    x = 0
    for i in numbers:
        if int(numbers[int(i)]) % 3 == 0:
            print("Числа, кратные 3: ", numbers[int(i)])
    for d in range(len(numbers) - 1):
        x += int(numbers[int(d)]) * int(numbers[int(d+1)])
    print("Произведение эл-ов: ",x)
    print(min(numbers))
