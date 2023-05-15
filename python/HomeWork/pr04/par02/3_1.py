
new_list1 = []
new_list2 = []

list3_5=[]


print ('Input 1 list ********')
while True:
    inpNumber=int(input('Input only integer (888 -Exit) in input ='))
    if inpNumber !=888:
        new_list1.append(inpNumber)
    else:
        break
           
print ('Input 2 ********')
while True:
    inpNumber=int(input('Input only integer (888 -Exit) in input ='))
    if inpNumber !=888:
        new_list2.append(inpNumber)
    else:
        break
print('You inputed  2 list')
print (new_list1,new_list2)

# третий список, содержащий элементы обоих списков
list3_1=new_list1+new_list2
print('The third list containing elements both lists')
print(list3_1)

# третий список, содержащий уникальные элементы каждого из списков
list3_2=list(list3_1)

countAllElements=len(list3_2)
i=0
while i <countAllElements:
        if list3_2.count(list3_2[i])>1:
            count_del=list3_2.count(list3_2[i])
            for j in range(count_del,1,-1):
                list3_2.remove(list3_2[i])
                i+=1
        countAllElements=len(list3_2)
        i+=1
print('The third list containing elements both lists without repetition')
print(list3_2)

# третий список, содержащий элементы общие для двух списков          
list3_temp=list(list3_1)
countAllElements=len(list3_temp)
list3_3=[]
# формируем список только из общих элементов (БУДУТ ПОВТОРЯЮЩИЕСЯ ЕЛЕМЕНТЫ)
i=0
while i <countAllElements:
        if list3_temp.count(list3_temp[i])>1:
            list3_3.append(list3_temp[i])
        i+=1
# удаляем повторяющиеся элементы 
countAllElements=len(list3_3)
i=0
while i <countAllElements:
        if list3_3.count(list3_3[i])>1:
            count_del=list3_3.count(list3_3[i])
            for j in range(count_del,1,-1):
                list3_3.remove(list3_3[i])
                i+=1
        countAllElements=len(list3_3)
        i+=1

print('The third list containing elements common to two lists')
print(list3_3)


# мин и макс значения каждого из списков

list3_5=[min(new_list1),max(new_list1),min(new_list2),max(new_list2)]

print('The third list containing only the minimum and maximum value of each lists')
print(list3_5)