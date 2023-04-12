number1=float(input ('Enter number1 : '))
number2=float(input ('Enter number2 : '))
if number1!=number2:
    if number1>number2:
        print(number2,number1)
    else:
        print(number1,number2)
else:
    print('The numbers are equal')
print ('Good bye')