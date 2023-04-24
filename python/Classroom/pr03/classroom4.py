from binascii import a2b_base64


a=int(input('input a:'))
b=int(input('input b:'))

while  b>=a:
    print(b,end=' ')
    b-=1