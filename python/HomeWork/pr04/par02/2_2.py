new_list = []
while True:
    inpNumber=int(input('Input only integer (888 -Exit) in input ='))
    if inpNumber !=888:
        new_list.append(inpNumber)
    else:
        break

countZero=0
countPozitiv=0
countNegativ=0
for i in range(len(new_list)):
    if new_list[i] ==0:
        countZero+=1
    elif new_list[i] >0:
        countPozitiv+=1
    elif new_list[i] <0:
        countNegativ+=1

print(new_list)
print('Min list item = ',min(new_list))
print('Max list item = ',max(new_list))
print ('Number of zero elements = ',countZero)
print ('Number of positive elements = ',countPozitiv)
print ('Number of negative elements = ',countNegativ)



