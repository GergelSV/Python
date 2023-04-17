numberMonth=int(input ('input number month(1-12): '))
if (numberMonth==12 or 1<=numberMonth<=2):
    print ('Winter')
elif (3<=numberMonth<=5):
    print ('Spring')
elif (6<=numberMonth<=9):
    print ('Summer')
elif (10<=numberMonth<=11):
    print ('Autumn')
else:
    print('invalid value')