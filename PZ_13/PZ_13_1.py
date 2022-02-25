# Даны значения роста 20 юношей. Определить сколько юношей будут направленны в баскетбольную команду (рост от 190)
# и сколько в футбольную (остальные)
from random import randint
people = []
for i in range(20):
    people.append(randint(160, 210))
print("Кол-во футболистов: ", len(list(filter(lambda x: x < 190, people))))
print("Кол-во баскетболистов: ", len(list(filter(lambda x: x >= 190, people))))
