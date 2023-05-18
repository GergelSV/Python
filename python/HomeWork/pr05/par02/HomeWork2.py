def Min_my(a):
    if type(a)==list:
        return min(a)


import random
mas = []

numb=int(input('Input the number of numbers in the list = '))
for i in range(numb):
    mas.append(random.randint(-250,250))

print('List:  ',mas)

print('Min = ',Min_my(mas))
