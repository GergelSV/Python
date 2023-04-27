stroka=input('Input text: ')

str1=stroka.replace('!!!','!')
str2=str1.replace('!!','!')
str3=str2.replace('...','.')

count_1=str3.count('.')
count_2=str3.count('?')
count_3=str3.count('!')

print('Number of offers = ',count_1+count_2+count_3)
