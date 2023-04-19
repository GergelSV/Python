a=int(input('input a:'))
b=int(input('input b:'))

print('Numbers in the range')
a0=a
mult5_count=0
while  a0<=b:
    print(a0,end=' ')
    if a0%5 ==0:
        mult5_count+=1
    a0+=1

print('\nNumbers in the range in descending order')
b0=b
while  b0>=a:
    print(b0,end=' ')
    b0-=1

print('\nNumbers in multiples of 7')
a0=a
while  a0<=b:
    if a0%7==0:
        print(a0,end=' ')
    a0+=1

print('\nThe count of numbers that are multiples of 5 =',mult5_count)