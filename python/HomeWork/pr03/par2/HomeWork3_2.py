count = 0
for i in range(100, 1000):
    a1=i//100
    a2=i//10%10
    a3=i%10
    if a1==a2 or a2==a3 or a1==a3:
        count+= 1
print('numbers 2 digits are the same = ',count)
