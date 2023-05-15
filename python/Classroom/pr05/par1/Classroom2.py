def oddNumOnInterval(a,b):
            
    for i in range(a+1,b):
            
            if i%2!=0:
                  print(i,end=' ')
            

number1=int(input ('input interval start: '))
number2=int(input ('input interval end: '))

oddNumOnInterval(number1,number2)
