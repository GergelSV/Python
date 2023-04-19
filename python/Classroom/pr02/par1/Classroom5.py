number1=int(input ('input number1: '))
number2=int(input ('input number2: '))
print('1- сумма двух чисел')
print('2- разница двух чисел')
print('3- среднеарефметическое двух чисел')
print('4- произведение двух чисел')
print(' ВВедите номер действия, что надо сделать:')
choose=int(input ())
if choose==1:
    print('сумма двух чисел =',number1+number2)
elif choose==2:
    print('разница двух чисел =',number1-number2)
elif choose==3:
    print('среднеарефметическое =',(number1+number2)/2)
elif choose==4:
    print('произведение двух чисел =',number1*number2)
else: print(' Вы сделали неправильный выбор')