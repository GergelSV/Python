def multiplicationOfNumbers(n1,n2):
    if n1>n2:
        n1,n2=n2,n1

 # формирование числового списка
    mas = []
    for i in range(n1,n2+1):
        mas.append(i)
    print('Incoming data ',mas)
 # вычисление произведения всех элементов   
    total = 1
    for i in range(n1,n2+1):
        total *= i
    return total

LowBorderRange=int(input('Input low border range = '))
UpperBorderRange=int(input('Input upper border range = '))

print('Multiplication number from range = ',multiplicationOfNumbers(LowBorderRange,UpperBorderRange))
