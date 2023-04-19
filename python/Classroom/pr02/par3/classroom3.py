n=int(input ('enter the 6th digit: '))
a=n%10
n //= 10
b=n%10
n //= 10
c=n%10
n //= 10
d=n%10
n //= 10
e=n%10
n //= 10
f=n%10
n //= 10
print (f,e,d,c,b,a)
if (f==0 or n):
    print ('No 6 digit')
else:
    if (a+b+c==d+e+f):
        print ('Lucky')
    else:
        print ('No lucky')

