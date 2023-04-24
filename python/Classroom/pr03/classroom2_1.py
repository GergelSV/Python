from binascii import a2b_base64


a=int(input('input a:'))
b=int(input('input b:'))
sum=0
i=0
while  a<=b:
    print(a,end=' ')
    sum+=a
    i+=1
    a+=1
else: 
    print('suma =',sum)
    print('arithmetic mean =',sum/i)