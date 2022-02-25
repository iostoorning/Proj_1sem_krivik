from random import randint
people = []
for i in range(20):
    people.append(randint(160, 210))
basketball = [n*1 for n in people if n >= 190]
football = []
print("Кол-во футболистов: ", len(set(people) - set(basketball)))
print("Кол-во баскетболистов: ", len(basketball))
