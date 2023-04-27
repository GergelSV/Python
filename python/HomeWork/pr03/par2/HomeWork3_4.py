n=int(input ('enter the digit: '))
buf=n
count=0
rez=0
#  узнаем скольки значное число результат в count
while  buf:
    count+=1
    buf//=10
#print (count)
buf=n
while count:
    number=buf%10
    print (number)
    buf//=10
    if not (number ==3 or number ==6):
        rez=rez+(number*10**count)
        print('rez',rez)
    count-=1
print(rez)

#number_of_signs=count
#for i in range(1,number_of_signs+1):
    
# a=n%10
# n //= 10
# b=n%10
# n //= 10
# c=n%10
# n //= 10
# d=n%10
# n //= 10
# e=n%10
# n //= 10
# f=n%10
# n //= 10
# print (f,e,d,c,b,a)
# if (f==0 or n):
#     print ('No 6 digit')
# else:
#     a,f = f,a
#     b,e = e,b
#     print (f,e,d,c,b,a)
