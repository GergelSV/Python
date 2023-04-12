number=int(input ('input  number : '))
a1=number//1000
a2=number//100%10
a3=number//10%10
a4=number%10
new_number=a4*1000+a3*100+a2*10+a1
print('********   program execution result    ********* ')
print('number1 = ',a1)
print('number2 = ',a2)
print('number3= ',a3)
print('number4 = ',a4)
print('inverted number = ',new_number)
