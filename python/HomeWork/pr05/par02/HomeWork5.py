def multiplicationOfNumbers (a):
    if type(a)==list:
        total=1
        for i in range(len(a)):
            total*=a[i]
        return total


import random
mas1 = []
mas2 = []

numb1=int(input('Input the number of numbers in the 1 list = '))
for i in range(numb1):
    mas1.append(random.randint(-250,250))

numb2=int(input('Input the number of numbers in the 2 list = '))
for i in range(numb2):
    mas2.append(random.randint(-250,50))
print('2 List:  ',mas2)


print('Multiplication of numbers lists = ',multiplicationOfNumbers(mas))
