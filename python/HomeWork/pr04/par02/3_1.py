
new_list1 = []
new_list2 = []


print ('Input 1 list ********')
while True:
    inpNumber=int(input('Input only integer (888 -Exit) in input ='))
    if inpNumber !=888:
        new_list1.append(inpNumber)
    else:
        break
           
print ('Input 2 list ********')
while True:
    inpNumber=int(input('Input only integer (888 -Exit) in input ='))
    if inpNumber !=888:
        new_list2.append(inpNumber)
    else:
        break

print('You inputed  2 list')
print (new_list1,new_list2)

ls1=list(new_list1)
ls2=list(new_list2)

# третий список, содержащий элементы обоих списков
list3_1=ls1+ls2
print('The third list containing elements both lists')
print(list3_1)

# третий список, содержащий элементы обоих списков без повторений
list3_2=list(ls1)
for item in ls2:
     if not item  in list3_2:
          list3_2.append(item)
print ('list containing elements of both lists without repetition',list3_2)
          

# третий список, содержащий элементы общие для двух списков          
list3_3=[]
for item in ls1:
    if item in ls2:
        list3_3.append(item)

print('The third list containing elements common to two lists')
print(list3_3)


# мин и макс значения каждого из списков
list3_5=[min(new_list1),max(new_list1),min(new_list2),max(new_list2)]

print('The third list containing only the minimum and maximum value of each lists')
print(list3_5)