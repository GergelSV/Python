def Max_my(a):
    if type(a)==list:
        return max(a)


import random

mas = []
for i in range(4):
    mas.append(random.randint(-250,250))

print('Incoming data ',mas)

print('Max = ',Max_my(mas))
