
print ('Угадай число  от 1 до 500')
# Программа загадала число
numberComp=250
count=0
number= int(input('Введите число от 1 до 500 (0 - Выход) - '))
while number!=0:
    if number>numberComp:
        print ('Ваше число больше, чем загаданное')
    elif number<numberComp:
        print ('Ваше число меньше, чем загаданное')
    elif number==numberComp:
        print ('Вы угадали !!!')
        count+=1
        break
    number= int(input('Введите число от 1 до 500 (0 - Выход) - '))
    count+=1
print('Количество попыток = ',count)




