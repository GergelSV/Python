class book:
        def __init__(self,name,year_release,pablisher,genre,author,price):
            self.name = name
            self.year_release = year_release
            self.pablisher = pablisher
            self.genre=genre
            self.author=author
            self.price=price
        
        def get_name(self):
              return self.name
        
        def get_year_release(self):
              return self.year_release
        
        def get_pablisher(self):
              return self.pablisher
        
        def get_genre(self):
              return self.genre
        
        def get_author(self):
              return self.author
        
        def get_price(self):
              return self.price
        
        def put_name(self,n):
              self.name=n
        
        def put_year_release(self,y):
              self.year_release=y
        
        def put_pablisher(self,pb):
              self.pablisher=pb
        
        def put_genre(self,g):
              self.genre=g
        
        def put_author(self,au):
              self.author=au
        
        def put_price(self,p):
             self.price=p
        
        def __str__(self) :
            return "This is a book " +self.name+"  "+str(self.year_release)+\
                  " year release with "+" pablisher "+self.pablisher+" genre "\
                  +self.genre+" and author "+self.author+" price = "+str(self.price)+" $"
        
                  
book1=book('Angels and Demons',2000,'Pocket Book','detective','Den Braun',10)

print(book1.get_author())
print(book1.get_name())

book1.put_genre('triller')

print(book1.__str__())