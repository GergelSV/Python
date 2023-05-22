n=int(input ('enter the digit: '))
buf=n
count=0
rez=0
#  узнаем скольки значное число результат в count
while  buf:
    count+=1
    buf//=10
buf=n
i=0
while count:
    number=buf%10
    buf//=10
    if not (number ==3 or number ==6):
        rez=rez+(number*10**i)
        i+=1
    count-=1
print('rezult =',rez )