def prime(a, b):
    if a == 0 or b == 0: 
         return max(a, b)
    else:
        if a > b:
            return prime(a - b, b)
        else:
            return prime(a, b - a)

Number1=int(input('Input 1 integer number= '))
Number2=int(input('Input 2 integer number= '))


print('Most-greater common divisor = ',prime(Number1,Number2))