print ('**********Exponentiation program************** ')
n=int(input ('Enter the number : '))
degree=int(input ('Enter the degree 0-7  : '))
if 0<=degree<=7:
    rez=n**degree
    print('Rezult=',rez)
else:
    print ('The degree out of range ')