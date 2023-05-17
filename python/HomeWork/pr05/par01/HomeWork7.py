def palindrome (a):
    lengthNumber=len(a)

    if len(a)%2==0:

        mas =[] 
        mas=list(a)
     
        part_1=mas[0:int((lengthNumber/2))]
        part_2=list(mas[int((lengthNumber/2)):int(len(a)+1)])
        part_2.reverse()


        if part_1==part_2:
            return True
        else:
            return False
    
 


Numb=input('Input integer number= ')

print('The number palindrom = ',palindrome (Numb))
