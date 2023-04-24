a=int(input('input a:'))
b=int(input('input b:'))
if a>b:
    a,b=b,a
while  a<=b:
    if a%2!=0:
        print(a,end=' ')
    a+=1
