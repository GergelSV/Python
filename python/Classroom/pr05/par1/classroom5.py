def SumRange(n1,n2):
    mas = []
    for i in range(n1,n2):
        mas.append(i)
    print('Incoming data ',mas)
    return sum(mas)

LowBorderRange=int(input('Input low border range = '))
UpperBorderRange=int(input('Input upper border range = '))

print('Sum number from range = ',SumRange(LowBorderRange,UpperBorderRange))
