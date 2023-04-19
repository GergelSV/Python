number1=int(input ('input number1: '))
number2=int(input ('input number2: '))
number3=int(input ('input number3: '))
print('1- sum of 3 numbers')
print('2- multiplication of 3 numbers')
print(' make a choice:')
choose=int(input ())
if choose==1:
    print('sum of 3 numbers =',number1+number2+number3)
elif choose==2:
    print('multiplication of 3 numbers',number1*number2*number3)
else: print(' You made the wrong choice')
print ('Good bye')