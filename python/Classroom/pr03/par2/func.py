def sumElements (a):
    if type(a)==list:
        return sum(a)
    
def MaxElements (a):
    if type(a)==list:
        return max(a)

def PrintZvezda(n):
    if n!=1:
        PrintZvezda(n-1)
    print('*',end='')

    