number=float(input('Input number or write 7 to stop the program: '))
sum=0
min_number=number
max_number=number
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
