def pow_for_list (ls,pow_):
    for i in range(len(ls)):
        ls[i]=pow(ls[i],pow_)
    return ls


import random
mas = []


numb=int(input('Input the number of numbers in the  list = '))
my_pow=int(input('Input the power to raise the numbers = '))

for i in range(numb):
    mas.append(random.randint(1,20))

print('List:  ',mas)
print('List of numbers raised to a power :',pow_for_list(mas,my_pow))