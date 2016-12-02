# -*- coding: utf-8 -*-

a = 3
b = 5
r = 0  # Чтобы было, чем заполнять
mas = []
for i in range(a):
    mas.append([])
    for j in range(b):
        mas[i].append(r)
        r += 1  # Чтобы заполнялось не одно и тоже

print(mas)
print ((mas[0][2    ]))