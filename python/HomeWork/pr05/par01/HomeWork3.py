def drawSquare(Length_Side, Simbol, Direction):
    if bool(Direction):
        for i in range(Length_Side):
            print(Simbol*Length_Side,end='')
            print()
    else:
        for i in range(Length_Side):
            if i==0:
                print(Simbol*Length_Side,end='')
                print()
            elif i==Length_Side-1:
                print(Simbol*Length_Side,end='')
            else:
                print(Simbol,' '*(Length_Side-4),Simbol)



intlength_side=int(input('Input line length side square - '))
intSimbol=input('Input character to fill the line - ')
intDirection=int(input('Input direction (0-empty 1-filled) -'))

drawSquare(intlength_side,intSimbol,intDirection)
