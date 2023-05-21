def isPrime(n):
    for i in range(2,n//2+1):
        if n % i == 0:
            return False
    else:
        return True

def numbersIsPrime(lst):
   count=0
   for i in range(len(lst)):
      if(isPrime(lst[i])):
          count+=1
   return count


import random
mas = []

numb=int(input('Input the number of numbers in the list = '))

for i in range(numb):
    mas.append(random.randint(1,25))

print('List:  ',mas)

print('Number of primes in the lists = ',numbersIsPrime(mas))
