def MinForFiveNumbers(a):
    if type(a)==list:
        return min(a)


import random

mas = []
for i in range(5):
    mas.append(random.randint(-250,250))

print('Incoming data ',mas)
print('Min number = ',MinForFiveNumbers(mas))
