def multiplicationOfNumbers (a):
    if type(a)==list:
        total=1
        for i in range(len(a)):
            total*=a[i]
        return total


import random
mas = []

numb=int(input('Input the number of numbers in the list = '))
for i in range(numb):
    mas.append(random.randint(-250,250))

print('List:  ',mas)

print('Multiplication of numbers lists = ',multiplicationOfNumbers(mas))
