class Car:
        def __init__(self,name,year,manufacturer,capacity,color,price):
            self.name = name
            self.year = year
            self.manufacturer = manufacturer
            self.capacity=capacity
            self.color=color
            self.price=price
        
        def get_name(self):
              return self.name
        
        def get_year(self):
              return self.year
        
        def get_manufacturer(self):
              return self.manufacturer
        
        def get_capacity(self):
              return self.capacity
        
        def get_color(self):
              return self.color
        
        def get_price(self):
              return self.price
        
        def put_name(self,n):
              self.name=n
        
        def put_year(self,y):
              self.year=y
        
        def put_manufacturer(self,m):
              self.manufacturer=m
        
        def put_capacity(self,c):
              self.capacity=c
        
        def put_color(self,cl):
              self.color=cl
        
        def put_price(self,p):
             self.price=p
        
        def __str__(self) :
            return "This is a car " +self.name+"  "+str(self.year)+" year release with "+" manufacturer "+self.manufacturer+" engine size "+str(self.capacity)+" and color "+str(self.color)+" price = "+str(self.price)+"  $"
        
                  
Avto=Car('Corola',2012,'Toyota',1.33,'Grey metalik',100000)
print(Avto.get_color())
print(Avto.get_name())

Avto.put_capacity(1.6)
print(Avto.__str__())