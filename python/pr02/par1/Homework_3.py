number_of_meters=int(input ('enter the number of meters: '))
print('1- miles')
print('2- inches ')
print('3- yards')
print(' make a choice:')
choose=int(input ())
if choose==1:
    print('the number of miles =',number_of_meters*0.000621371)
elif choose==2:
    print('the number of inches =',number_of_meters*39.3701)
elif choose==3:
    print('the number of yards = ',number_of_meters*1.09361)  
else: print(' You made the wrong choice')
print ('Good bye')