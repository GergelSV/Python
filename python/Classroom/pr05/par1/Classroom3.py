def drawAline(Length_Line, Simbol, Direction):
    if Direction==0:
        count=0
        while count<Length_Line:
            print(Simbol,end='')
            count+=1
    else:
        count=0
        while count<Length_Line:
            print('                         ',Simbol,sep='                      ')
            count+=1


intlength_line=int(input('Input line length - '))
intSimbol=input('Input character to fill the line - ')
intDirection=int(input('Input direction (0-horizontal 1-vertical) -'))

drawAline(intlength_line,intSimbol,intDirection)
