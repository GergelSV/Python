print('********************************* ПОШУК ПРОСТОГО ************************************************')
a=int(input('Введіть початкове значення  інтервалу: '))
b=int(input('Введіть кінцеве значення  інтервалу: '))
if a==1:
    a=2
for n in range (a,b+1):
   i=2
   while i*i<n:
      if n%i==0:
         break
      i+=1
   else:
      print (n,end=' ')
   






         
   
    