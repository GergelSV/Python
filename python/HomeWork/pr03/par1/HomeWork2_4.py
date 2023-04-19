min_number=0
max_number=0
sum=0
number=float(input('Input number or write 7 to stop the program: '))
while True:
    if number ==7:
        break
    else:
        sum+=number
        if number>max_number:
            max_number=number
        elif number<min_number:
            min_number=number
    number=float(input('Input number or write 7 to stop the program: '))
print('Suma = ',sum)
print('Mininal number =',min_number)
print('Maximal number =',max_number)
print('Good bye')
