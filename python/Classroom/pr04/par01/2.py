stroka=input('Input str: ')
len_str=len(stroka)

count_dig=0
count_chr=0

for i in range(1,len_str+1):
    if '0'<=stroka[i-1]<='9':
        count_dig+=1
    elif 'a'<=stroka[i-1]<='z' or 'A'<=stroka[i-1]<='Z':
        count_chr+=1

print('Count Char = ', count_chr)
print('Count Digital = ', count_dig)