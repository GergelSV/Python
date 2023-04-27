
answer= input('Будем менять деньги (Да, Нет) - ')
while answer=='Да':    
    sum_grn=float(input('Введите сумму в грн : '))
    sum_usa=sum_grn/40
    print('Ваша сумма в $ =',sum_usa)
    answer= input('Будем менять деньги (Да, Нет) - ')


