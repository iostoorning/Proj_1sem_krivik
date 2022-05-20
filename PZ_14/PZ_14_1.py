# В исходном текстовом файле (Dostoevsky.txt) найти все годы деятельности писателя
# (например, 1821 года, 1837 год, 1843 году и так далее по всему тексту). Посчитать
# Посчитать кол-во элементов
import re
buf = open("Dostoevsky.txt", "r")
text = buf.read()
result = re.findall(r'год', text)
print(len(result))
