
lst=(input(' Input expression '))

if   lst.find('+')!=-1:
    lstOperands=lst.split('+')
    rezult=float(lstOperands[0])+(float(lstOperands[1]))
elif  lst.find('-')!=-1:
    lstOperands=lst.split('-')
    rezult=float(lstOperands[0])-(float(lstOperands[1]))
elif  lst.find('*')!=-1:
    lstOperands=lst.split('*')
    rezult=float(lstOperands[0])*(float(lstOperands[1]))
elif  lst.find('/')!=-1:
    lstOperands=lst.split('/')
    rezult=float(lstOperands[0])/(float(lstOperands[1]))


print(lst,' = ',rezult)


