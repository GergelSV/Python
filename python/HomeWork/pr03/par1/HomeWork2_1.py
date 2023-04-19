a=int(input('input a:'))
b=int(input('input b:'))
sum_even=0
sum_noteven=0
sum_mult9=0
count_even=0
count_noteven=0
count_mult9=0
while  a<=b:
        if a%2 ==0:
            sum_even+=a
            count_even+=1
        else:
            sum_noteven+=a
            count_noteven+=1
        if a%9 ==0:
             sum_mult9+=a
             count_mult9+=1
        a+=1
print('Sum of even numbers =',sum_even)
print('Sum of  not even numbers =',sum_noteven)
print('Sum numbers in multiples 9  =',sum_mult9)
print('Arithmetic  mean metic of even numbers = ',sum_even/count_even)
print('Arithmetic  mean metic of  not even numbers = ',sum_noteven/count_noteven)
print('Arithmetic  mean metic of multiples 9 = ',sum_mult9/count_mult9)