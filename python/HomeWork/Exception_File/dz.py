def print_spis (str_header1,str_header2,spisok):
    print('\n\n')
    i = 1
    print (str_header1)
    print (str_header2)
    for student in spisok:
        print (i,'. ',student[0],'\t ',student[1],'\t ',student[2])
        i += 1
    print('\n')

def removeStudent(fileIn, StudentNumber):
    file_Temp = './student_temp.txt'
    with open(fileIn,'r') as fr:
        students = fr.readlines()
 
        counter=1 # position pointer 
 
        with open(file_Temp, 'w') as fw:
            for student in students:
                if counter != StudentNumber:
                    fw.write(student)
                counter += 1
        
    with open(file_Temp) as inFile, open(fileIn, "w") as outFile:
        fileContents = inFile.read()
        outFile.write(fileContents)    



        
 
answer_number=1
while answer_number==1:
    print('\n\n\n\n\n')
    print ('Програма для роботи зі студентами нашої групи. ')
    print('Ви можете:')
    print()
    print ('1. Додати студента')
    print ('2. Видалити студента')
    print ('3. Змінити інформацію про студента')
    print ('4. Показати на екрані ВСІХ студентів')
    print ('5. Виконати пошук студента')
    print ('6. Вивести студентів в певному порядку')
    print ('7. Вивести "відмінників" (з середнім балом 10+)')
    print('')

    try:
            action=int(input('Оберіть дію: (1-7) :'))      
            if action < 1 or action > 7:
                raise Exception (" !!!! Ви ввели невірний номер дії.\n Завершення роботи програми.")
             
    except  ValueError:
            print(" !!!! Повинні бути тільки цифри 1 або 7.\n Завершення роботи програми.")
            break
    except Exception as ex:
            print(ex)
            break
    #########

    try:
        fin = open('./students.txt','r') 
        f_students = fin.readlines()
        marks = []
        sp_student = []
        for student in f_students:
            tmp = student.split()
            sp_student.append(tmp)
            marks.append(float(tmp[2]))
        #print(marks)
        #print(sp_student)   
    except Exception as ex:
        print(ex)
    finally:
        fin.close()


    if action==1:
        #  ДІЯ - додати студента
            
        try:
            Surname_st = input('введіть прізвище студента : ')
            if len(Surname_st) == 0:
                raise Exception ("!!!! прізвище студента не може бути порожнім")    
            
            Name_st = input("введіть ім'я студента : ")     
            if len(Name_st) == 0:
                raise Exception ("!!!! ім'я студента не може бути порожнім") 
            
            AVG_marks = int(input('введіть середній бал успішності (1-12) :'))                
            if AVG_marks < 1 or AVG_marks > 12:
                raise Exception ("!!!! Середній бал успішності не може дорівнювати "+str(AVG_marks))
            
        except  ValueError:
            print(" !!!! Середній бал успішності - повинно містити тільки цифри")
        except Exception as ex:
            print(ex)
        
        sp_tmp = [] 
        sp_tmp = list((Surname_st,Name_st,AVG_marks))
        sp_student.append(sp_tmp)
        
        #fin = open('./students.txt','r') 
        with open('./students.txt', 'w') as fw:
            for student in sp_student:
                fw.write(str(student))
               
    elif action == 2:
        # ДІЯ  - видалити студента
        
        str1 = '\t\tСписок ВСІХ студентів'
        str2 = "N   Призвище \t   Ім'я \tсередній бал " 
        print_spis (str1,str2,sp_student)
        # виклик функціі підрахунка кількості студентів  = COUNT 
        try:
            Number_del = int(input('Введіть номер студента, якого потрібно видалити: '))      
            if Number_del < 1 or Number_del > len(sp_student):       
                raise Exception (" !!!! Студента з таким номер за списком не існує.\n Завершення роботи програми.")
             
        except  ValueError:
            print(" !!!! Повинні бути тільки цифри.\n Завершення роботи програми.")
            break
        except Exception as ex:
            print(ex)
            break

        myFile='./students.txt'
        #resultFile='./studentsout.txt'
        
        removeStudent(myFile, Number_del)

    elif action == 3:

        # ДІЯ  - змінити інформацію про студента
        pass
    elif action == 4:
        # ДІЯ  - показати на екрані ВСІХ студентів

        str1 = '\t\tСписок ВСІХ студентів'
        str2 = "N   Призвище \t   Ім'я \tсередній бал " 
        print_spis (str1,str2,sp_student)
        
        
    elif action == 5:
        # ДІЯ - вивести на екран інформацію про студента, виконавши пошук за вказаним параметром /
        #       (прізвище, ім'я, середній бал успішності)  
        pass
    elif action == 6:
        # ДІЯ - Вивести студентів в певному порядку (за алфавітом, за середнім балом успішності)    
        print('\n\n\n\n\n\n\n\n')
        print ('1. Вивести студентів за алфавітом')
        print ('2. Вивести студентів за середнім балом успішності')
        print('\n\n')
        try:
            action_6 = int(input('Оберіть дію: (1-2) :'))      
            if action_6 < 1 or action_6 > 2:
                raise Exception (" !!!! Ви ввели невірний номер дії.\n Завершення роботи програми.")
             
        except  ValueError:
            print(" !!!! Повинні бути тільки цифри 1 або 2.\n Завершення роботи програми.")
            break
        except Exception as ex:
            print(ex)
            break
        
        if action_6 == 1:
            #  ДІЯ - Вивести студентів за алфавітом
            pass  
        elif action_6 == 2: 
            pass
            
    elif action == 7:
        # ДІЯ - Вивести "відмінників" (з середнім балом 10+)
        excellent_student = []
        for student in sp_student:
            if float(student[2]) > 10:
                excellent_student.append(student)
            

        str1 = 'Список "відмінників" (з середнім балом 10+)'
        str2 = "N   Призвище \t   Ім'я \tсередній бал " 
        print_spis (str1,str2,excellent_student)
        

    # else:
    #     print('Ви ввели невірний номер дії')
    try:
        answer_number=int(input('Попрацюємо  ще?  (1- Так 0 - Ні)  '))           
        print('')
        if answer_number != 1:
            print(' До побачення. ')
            break
    except ValueError:
            print(" !!!! Введено дані відмінні від 1 або 0.\n *****Завершення роботи програми.******")
            break

