time_sek=int(input ('input time in seconds: '))
print('1- time in hours until the end of the day')
print('2- time in minutes until the end of the day')
print('3- time in seconds until the end of the day')
print(' make a choice:')
choose=int(input ())
if choose==1:
    print('time in hours until the end of the day =',(86400-time_sek)//60//60)
elif choose==2:
    print('time in minutes until the end of the day =',(86400-time_sek)//60)
elif choose==3:
    print('time in seconds until the end of the day =',(86400-time_sek))

else: print(' You made the wrong choice')