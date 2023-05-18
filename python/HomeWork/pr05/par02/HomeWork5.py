def elements_of_two_lists (ls1,ls2,ls3):
    
    ls3=ls1+ls2
    return ls3


import random
mas1 = []
mas2 = []
mas12= []

numb1=int(input('Input the number of numbers in the 1 list = '))
for i in range(numb1):
    mas1.append(random.randint(-250,250))

numb2=int(input('Input the number of numbers in the 2 list = '))
for i in range(numb2):
    mas2.append(random.randint(-250,50))

print('1 List:  ',mas1)
print('2 List:  ',mas2)

print('The third list containing elements common to two lists',elements_of_two_lists(mas1,mas2,mas12))