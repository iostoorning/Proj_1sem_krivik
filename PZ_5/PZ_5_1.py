while True:
    try:
        a = 0


        def charnumber(x):
            x = len(input("Введите символы "))
            print(x)


        charnumber(a)
        break
    except ValueError:
        print("Ошибка значения! Введите символы")
