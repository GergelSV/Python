a=int(input('input a:'))
b=int(input('input b:'))

while  a<=b:
    if a%3==0:
        if a%5==0:
            print ('Fizz Buzz')
        else:
            print ('Fizz')
    elif a%5==0:
        print ('Buzz')
    else:
        print(a)
    a+=1
