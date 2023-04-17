n=int(input ('Enter a number between 1 and 100: '))
if 0<=n<=100:
    if n%3==0:
        if n%5==0:
            print ('Fizz Buzz')
        else:
            print ('Fizz')
    elif n%5==0:
        print ('Buzz')
    else:
        print('number :',n)
else:
    print ('The number out of range ')