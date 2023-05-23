def pow_for_list (ls,pow_):
    
    ls_pow=[]
    
    for i in range(len(ls)):
        ls_pow.append(pow(ls[i],pow_))
    
    return ls_pow


import random
mas = []


numb=int(input('Input the count of numbers in the  list = '))
my_pow=int(input('Input the power to raise the numbers = '))

for i in range(numb):
    mas.append(random.randint(1,10))

print('List:  ',mas)
print('List of numbers raised to a power :',pow_for_list(mas,my_pow))