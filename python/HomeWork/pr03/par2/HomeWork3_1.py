x=int(input('Input X :'))
y=int(input('Input Y :'))
x_degree_y=x
for i in range(1, y):
    x_degree_y*=x
print('Number X to the degree Y = ',x_degree_y)
