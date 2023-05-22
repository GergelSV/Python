answer_number=1
while answer_number==1:
    n=int(input('Введіть довжину сторони квадрата =  '))
    figure=int(input('Введіть яку фігуру бажаєте вивести (1-5) :'))
    if figure==1:
        # фігура А
        for i in range(n):
            print(' '*i,'*'*(n-i),sep='')
    elif figure==2:
        # фігура Б
        for i in range(n+1):
            print(' '*(n-1),'*'*i,sep='')
    elif figure==3:
        # фігура В
        for i in range(-1,n//2-1):
            print(' '*(i+1),'*'*(n-2*(i+1)),' '*(i+1),sep='')
        for i in range(n//2):
            print (' '*n)
    elif figure==4:
        # фігура Г
        for i in range(n//2-1):
            print (' '*n)
        for i in range(n//2-1,-2,-1):
            print(' '*(i+1),'*'*(n-2*(i+1)),' '*(i+1),sep='')
    elif figure==5:
        # фігура Д
        for i in range(-1,n//2-1):
            print(' '*(i+1),'*'*(n-2*(i+1)),' '*(i+1),sep='')
        for i in range(n//2-2,-2,-1):
            print(' '*(i+1),'*'*(n-2*(i+1)),' '*(i+1),sep='')
    else:
        print('Ви ввели неправильний номер ')
    
    answer_number=int(input('Попрацюємо  ще?  (1- Так 0 - Ні)  '))
    if answer_number==0:
        print(' До побачення. ')
        break
