sale1Manager=int(input ('Enter sale of 1 manager : '))
sale2Manager=int(input ('Enter sale of 2 manager : '))
sale3Manager=int(input ('Enter sale of 3 manager : '))
# расчет з-п 1 менеджера
if 0<=sale1Manager<500:
    salary1Manager=200+(200/100*3)
elif 500<=sale1Manager<1000:
        salary1Manager=200+(200/100*5)
elif sale1Manager>1000:
        salary1Manager=200+(200/100*8)
else:
    print ('The sale of 1 manager out of range ')
# расчет з-п 2 менеджера
if 0<=sale2Manager<500:
    salary2Manager=200+(200/100*3)
elif 500<=sale2Manager<1000:
        salary2Manager=200+(200/100*5)
elif sale2Manager>1000:
        salary2Manager=200+(200/100*8)
else:
    print ('The sale of 2 manager out of range ')
# расчет з-п 3 менеджера
if 0<=sale3Manager<500:
    salary3Manager=200+(200/100*3)
elif 500<=sale3Manager<1000:
        salary3Manager=200+(200/100*5)
elif sale3Manager>1000:
        salary3Manager=200+(200/100*8)
else:
    print ('The sale of 3 manager out of range ')
# определение лучшего работника
if salary1Manager != salary2Manager and salary1Manager!=salary3Manager and salary2Manager!=salary3Manager:
    if salary1Manager>salary2Manager and salary1Manager>salary3Manager:
        salary1Manager=salary1Manager+200
    elif salary2Manager>salary1Manager and salary2Manager>salary3Manager:
        salary2Manager=salary2Manager+200
    else:
        salary3Manager=salary3Manager+200    
else:
    print('It is impossible to determine the best employee')
print('Salary 1 manager =',salary1Manager)
print('Salary 2 manager =',salary2Manager)
print('Salary 3 manager =',salary3Manager)