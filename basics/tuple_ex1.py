a = 1, 2, 3, 4
print(a)
print(type(a))

x, y, *z = 1,2,3,4,5,6
print(x ,y, z)
print(type(x),type(y),type(z))

x = (23,45,21,45)
y = tuple([3,2,1,5])  #converting a list to tuple

print(x,y)
print(type(x),type(y))