def print_spisok (str_header,spisok):
    
    nomer_pp = 1
    
    print('\n\n')
    print (str_header)
    print('---------------------------------------------')
    print("N   Призвище \t   Ім'я \tсередній бал ")
    print('---------------------------------------------')    
    
    for student in spisok:
        print (nomer_pp,'. ',student[0],'\t ',student[1],'\t ',student[2])
        nomer_pp += 1
    print('\n')

def print_find_student():
    
    str1 = '\n\n Інформація про знайденого студента'
    print('\n\n')
    
    print_spisok (str1,find_student)


###### body
try:
        fin = open('./students.txt','r') 
        f_students = fin.readlines()
        
        sp_student = []
        for student in f_students:
            tmp = student.split()
            tmp[2] = float(tmp[2])
            sp_student.append(tmp)
           
         
except Exception as ex:             
        print(ex)
finally:
        fin.close()


        
 
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
    print ('8. Вихід')
    print ('')
    try:
            action=int(input('Оберіть дію: (1-8) :'))      
            if action < 1 or action > 8:
                raise Exception (" !!!! Ви ввели невірний номер дії.\n *****Завершення роботи програми.******")
             
    except  ValueError:
            print(" !!!! Повинні бути тільки цифри від 1 до 8.\n *****Завершення роботи програми.******")
            buf = input('Press any key.....' )
            break   
    except Exception as ex:
            print(ex)
            buf = input('Press any key.....' )
            break   
        
                
    ######### опрацювання пунктів меню
    
    if action==1:
        #  ДІЯ - додати студента
        try:
            Surname_st = input('введіть прізвище студента : ')
            if len(Surname_st) == 0:
                raise Exception ("!!!! прізвище студента не може бути порожнім")    
                
            Name_st = input("введіть ім'я студента : ")     
            if len(Name_st) == 0:
                raise Exception ("!!!! ім'я студента не може бути порожнім") 
                
            AVG_marks = float(input('введіть середній бал успішності (1.0-12.0) :'))                
            if AVG_marks < 1 or AVG_marks > 12:
                raise Exception ("!!!! Середній бал успішності не може дорівнювати "+str(AVG_marks))
                
        
        
        except  ValueError:
            print(" !!!! Середній бал успішності - повинен містити тільки цифри")
            buf = input('Press any key.....' )
            continue
        except Exception as ex:
            print(ex)
            buf = input('Press any key.....' )
            continue

        sp_tmp = [] 
        sp_tmp = list((Surname_st,Name_st,AVG_marks))    
        sp_student.append(sp_tmp)
                
    elif action == 2:
        # ДІЯ  - видалити студента
        
        str1 = '\t\t Список ВСІХ студентів'        
        print_spisok (str1,sp_student)
       
        try:
            Number_del = int(input('Введіть номер студента, якого потрібно видалити: '))      
            if Number_del < 1 or Number_del > len(sp_student):       
                raise Exception (" !!!! Студента з таким номер за списком не існує.")
             
        except  ValueError:
            print(" !!!! Повинні бути тільки цифри.")
            buf = input('Press any key.....' )
            continue
        except Exception as ex:
            print(ex)
            buf = input('Press any key.....' )
            continue
        
        sp_student.pop(Number_del-1)
        print ('\n\n Студента за порядковим номером ',Number_del,'видалено успішно.\n\n')       
        

    elif action == 3:
     #ДІЯ  - змінити інформацію про студента
        
        str1 = '\t\t Список ВСІХ студентів'
        print_spisok (str1,sp_student)
        
        try:
            Nomer_pp = int(input('Введіть номер студента по списку у якого будемо змінювати інформацію: '))      
            if Nomer_pp < 1 or Nomer_pp > len(sp_student):
                raise Exception ("!!!! номер студетна у списку не може дорівнювати "+str(Nomer_pp))
             
                
            Surname_st = input('введіть прізвище студента : ')
        
            if len(Surname_st) == 0:
                raise Exception ("!!!! прізвище студента не може бути порожнім")    
                
            Name_st = input("введіть ім'я студента : ")     
            if len(Name_st) == 0:
                raise Exception ("!!!! ім'я студента не може бути порожнім") 
                
            AVG_marks = float(input('введіть середній бал успішності (1.0-12.0) :'))                
            if AVG_marks < 1 or AVG_marks > 12:
                raise Exception ("!!!! Середній бал успішності не може дорівнювати "+str(AVG_marks))
             
                
        except  ValueError:
                print ("!!!! Повинні бути тільки цифри.")
                buf = input('Press any key.....' )
                continue    
        except Exception as ex:
                print(ex)
                buf = input('Press any key.....' )
                continue

        sp_student[Nomer_pp-1] = list((Surname_st,Name_st,AVG_marks)) 
        print ('\n\n Дані студента за порядковим номером ',Nomer_pp,'змінено успішно.\n\n')  

    elif action == 4:
        # ДІЯ  - показати на екрані ВСІХ студентів

        str1 = '\t\t Список ВСІХ студентів'
        print_spisok (str1,sp_student)
        
        
    elif action == 5:
        # ДІЯ - вивести на екран інформацію про студента, виконавши пошук за вказаним параметром /
        #       (прізвище, ім'я, середній бал успішності)  
        print('\n\n\n\n\n\n\n\n')
        print ('Пошук  студента за  вказаним параметром :')
        print ('1. За номером у списку')
        print ('2. Прізвище')
        print ("3. Ім'я")
        print ('4. середній бал успішності')
        print('\n\n')
               
        try:
            action_5 = int(input('Введіть номер  дії (1-4) :'))      
            if action_5 < 1 or action_5 > 4:
                raise Exception 
             
        except  (ValueError,Exception):
            continue
        
        if action_5 == 1:
            #  ДІЯ - Вивести студента
            try:
                Nomer_pp = int(input('Введіть номер студетна у списку:'))      
                if Nomer_pp < 1 or Nomer_pp > len(sp_student)-1:
                    raise Exception ("!!!! номер студетна у списку не може дорівнювати "+str(Nomer_pp))
             
            except  ValueError:
                print ("!!!! Повинні бути тільки цифри.")
                buf = input('Press any key.....' )
                continue    
            except Exception as ex:
                print(ex)
                buf = input('Press any key.....' )
                continue
                
            # вивід інформації про  знайденого студента 
            
            find_student = sp_student[Nomer_pp-1:Nomer_pp]
            print_find_student()
            
        
        elif action_5 == 2: 
            try:
                Surname_st = input('введіть прізвище студента : ')
                if len(Surname_st) == 0:
                    raise Exception ("!!!! прізвище студента не може бути порожнім")    
            except Exception as ex:
                print(ex)
                buf = input('Press any key.....' )
                continue
            
            find_student = []
            for student in sp_student:
                if Surname_st in student[0:]:                                  
                   find_student.append(student)
            print_find_student()                       
            
            
        elif action_5 == 3: 
            try:
                Name_st = input("введіть ім'я студента : ")
                if len(Name_st) == 0:
                    raise Exception ("!!!! ім'я студента не може бути порожнім")    
            except Exception as ex:
                print(ex)
                buf = input('Press any key.....' )
                continue
            
            find_student = []
            for student in sp_student:
                if Name_st in student[1:]:                                  
                   find_student.append(student)
            print_find_student()                       
            
        
        elif action_5 == 4: 
                
            try:
                AVG_marks = float(input("введіть середній бал успішності студента (1-12): "))
                if AVG_marks < 1 or AVG_marks > 12:
                    raise Exception ("!!!! Середній бал успішності не може дорівнювати "+str(AVG_marks))
            
            except  ValueError:
                print(" !!!! Середній бал успішності - повинен містити тільки цифри")
            except Exception as ex:
                print(ex)
                buf = input('Press any key.....' )
                continue
            
            find_student = []
            for student in sp_student:                               
                if AVG_marks in student[2:]:                                  
                   find_student.append(student)
            
            print_find_student()     


    elif action == 6:
        # ДІЯ - Вивести студентів в певному порядку (за алфавітом, за середнім балом успішності)    
        
        print('\n\n\n\n\n\n\n\n')
        print ('1. Вивести студентів за алфавітом')
        print ('2. Вивести студентів за середнім балом успішності')
        print('\n\n')
        
        try:
            action_6 = int(input('Оберіть дію: (1-2) :'))      
            if action_6 < 1 or action_6 > 2:
                raise Exception (" !!!! Введено дані відмінні від 1 або 0.")
             
        except ValueError:
            print(" !!!! Повинен містити тільки цифри")
            buf = input('Press any key.....' )
            continue
            
        except Exception as ex:
                print(ex)
                buf = input('Press any key.....' )
                continue
           
        if action_6 == 1:
            #  ДІЯ - Вивести студентів за алфавітом
           
            sp_surname = []
            sp_surname  = sorted(sp_student, key=lambda student: student[0])
            
            str1 = '\t Список студентів за прізвищем'
            print_spisok (str1,sp_surname )   
        
        elif action_6 == 2: 
            #  ДІЯ - Вивести студентів за середнім балом
            
            sp_marks = []
            sp_marks  = sorted(sp_student, key=lambda student: student[2])
            
            str1 = 'Список студентів за середнім балом успішності'
            print_spisok (str1,sp_marks ) 
            
    elif action == 7:
        # ДІЯ - Вивести "відмінників" (з середнім балом 10+)
        
        excellent_student = []
        
        for student in sp_student:
            if student[2] > 10:
                excellent_student.append(student)
            

        str1 = 'Список "відмінників" (з середнім балом 10+)'
        print_spisok (str1,excellent_student)
    
    elif action == 8: 
        print(' До побачення. ')
        break


    
    try:
        answer_number=int(input('Попрацюємо  ще?  (1- Так 0 - Ні)  '))           
        print('')
        if answer_number != 1:
            print(' До побачення. ')
            break
    except ValueError:
            print(" !!!! Введено дані відмінні від 1 або 0.\n *****Завершення роботи програми.******")
            break
    finally:
            with open('./students.txt', 'w') as fw:   
                for student in sp_student:
                    fw.write(' '.join(map(str,student)))
                    fw.write('\n')

