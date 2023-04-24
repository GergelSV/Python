count = 0
for i in range(100, 10000):
    a1=i//1000
    a2=i//100%10
    a3=i//10%10
    a4=i%10
    if a1!=a2 and a2!=a3 and  a1!=a3 and a1!=a4 and a2!=a4 and a3!=a4:
        count+= 1
print('All numbers are different = ',count)
