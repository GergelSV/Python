# student = ['Dmytro', 'Medvediev', '37']
# st = student
# print(student, st)
# st.append(1234)
# print(student, st)
# a = 5
# b = a
# b = 7
# print(a)
# # student2 = ['123', 'surname', ' 37']

# # grupa = [student, student2, 23]
# # print(student[2])
# # name = student[0]
# # surname = student[1]
# # # student.append('068','066')
# # print(name, surname)
# # print(grupa[0][2])

# # new_list = []
# # nlist = (student+student2)*3
# # print(nlist)
# # nlist[2:6] = '1',1,1,1,1,1
# # print(nlist)
# # del nlist[2:8]
# # print(nlist)


# # n = nlist.pop()
# # print(nlist)
# # print('n = ',n)


# # nlist.insert(8, 'NEW')
# # print(nlist)

# # New_list  = nlist[::-1]
# # print(New_list)



n = int(input('count of number: '))
lst = []
for i in range(n):
    lst.append(int(input('number['+str(i)+'] = ')))
 
print('Suma= ',sum(lst))
print('Среднеарефметическое = ',sum(lst)/n)
