a=int(input('Input lower range limit: '))
b=int(input('Input high range limit: '))
number=int(input('Input number from range limit: '))
while a>number or number>b:
    number=int(input('Re-enter the number: '))
for i in range(a,b+1):
    if  i==number:
        print('!',i,'!',end=' ')
    else:
        print (i, end=' ')
    