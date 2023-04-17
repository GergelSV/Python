moboper11=float(input ('Стоимость звонков с Киевстар (1) на Киевстар (1): '))
moboper12=float(input ('Стоимость звонков с Киевстар (1) на Водафон (2): '))
moboper13=float(input ('Стоимость звонков с Киевстар (1) на Лайф (3): '))
moboper22=float(input ('Стоимость звонков с Водафон (2) на Водафон (2): '))
moboper21=float(input ('Стоимость звонков с Водафон (2) на Киевстар (1): '))
moboper23=float(input ('Стоимость звонков с Водафон (2) на Лайф (3): '))
moboper33=float(input ('Стоимость звонков с Лайф (3) на Лайф (3): '))
moboper31=float(input ('Стоимость звонков с Лайф (3) на Киевстар (1): '))
moboper32=float(input ('Стоимость звонков с Лайф (3) на Водафон (2): '))
out_call=int(input('Введите моб.оператора (1-3) с которого  звонить - '))
in_call=int(input('Введите моб.оператора (1-3) на который звонить - '))
if 1<=out_call<=3 and 1<=in_call<=3:
    choose_tarif='moboper'+str(out_call)+str(in_call)
    if choose_tarif=='moboper11':
        print ('стоимость звонков = ',moboper11)
    elif choose_tarif=='moboper12':
        print ('стоимость звонков = ',moboper12)
    elif choose_tarif=='moboper13':
        print ('стоимость звонков = ',moboper13)
    elif choose_tarif=='moboper21':
        print ('стоимость звонков = ',moboper21) 
    elif choose_tarif=='moboper22':
        print ('стоимость звонков = ',moboper22) 
    elif choose_tarif=='moboper23':
        print ('стоимость звонков = ',moboper23)   
    elif choose_tarif=='moboper31':
        print ('стоимость звонков = ',moboper31) 
    elif choose_tarif=='moboper32':
        print ('стоимость звонков = ',moboper32) 
    elif choose_tarif=='moboper33':
        print ('стоимость звонков = ',moboper33)  
else:
    print ('Неверно введено номер оператора')
