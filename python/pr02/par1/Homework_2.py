number1=int(input ('input number1: '))
number2=int(input ('input number2: '))
number3=int(input ('input number3: '))
print('1- max of 3 numbers')
print('2- min of 3 numbers')
print('3- arithmetic mean of 3 numbers')
print(' make a choice:')
choose=int(input ())
if choose==1:
    print('max of 3 numbers =',max(number1,number2,number3))
elif choose==2:
    print('min of 3 numbers',min(number1,number2,number3))
elif choose==3:
    print('arithmetic mean of 3 numbers',(number1+number2+number3)/3)  
else: print(' You made the wrong choice')
print ('Good bye')