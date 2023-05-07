stroka=input('Введіть рядок: ')
stroka_new=stroka.replace(' ','')
stroka_a=stroka_new.lower() 
stroka_b=stroka_a[::-1]
if stroka_a==stroka_b:
    print ('Введений рядок є паліндромом')
else:
    print ('Введений рядок не є паліндромом')
 

