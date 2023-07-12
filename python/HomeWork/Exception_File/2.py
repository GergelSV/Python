fin = open('./students.txt','r')
f_students = fin.readlines()
marks = []
sp_student = []
for student in f_students:
    tmp = student.split()
    tmp[2] = float(tmp[2])
    sp_student.append(tmp)
print (sp_student)
    # marks.append(float(tmp[2]))
marks = sorted(sp_student, key=lambda student: student[2])

print(marks)

# sort_spis = []
# sort_spis = sp_student.sort()
# print (sort_spis)