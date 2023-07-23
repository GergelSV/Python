fin = open('./2.txt','r') 
f_students = fin.readlines()
marks = []
sp_student = []
for student in f_students:
    tmp = student.split()
    sp_student.append(tmp)
    marks.append(float(tmp[2]))
print(sp_student)
sp_student.pop(1)  
print(sp_student)

with open('./students1.txt', 'w') as fw:
    for student in sp_student:
        fw.write(' '.join(map(str,student)))
        fw.write('\n')


sp_student.pop(1)   