print('********************************* ТАБЛИЦЯ МНОЖЕННЯ ************************************************')
begin_tabl=int(input('Введіть початкове значення : '))
end_tabl=int(input('Введіть кінечне значення : '))
for i in range(begin_tabl,end_tabl+1):
    for j in range(1,11):
        print (i,'*',j,'=',i*j,end='  ')
    print('\n')
   
    