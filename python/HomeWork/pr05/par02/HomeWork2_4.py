def countDeleteNumber(lst,delN):
    li = []

    for i in lst:
        if i !=delN:
            li.append(i)
    return len(lst)-len(li)

mas = []

number=int(input('Input the number of numbers in the list = '))
for i in range(number):
    mas.append(int(input('number['+str(i)+'] = ')))
delNumber=int(input('Input the number to be removed = '))

print('List:  ',mas)
print('Count of delete number = ',countDeleteNumber(mas,delNumber))
