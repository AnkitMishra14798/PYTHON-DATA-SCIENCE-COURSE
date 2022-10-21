# tuple - set - list (interchangeable)

x = [1,2,3,4,5,5,6,6,7]

xt = tuple(x) #list -> tuple
xl = list(xt) #tuple -> list
xs = set(x) # list -> list
xl = list(x) # set -> list
xs = set(x) # tuple -> set
xt = tuple(x) # set -> tuple

x = []
for i in range(10):
    a= (input("enter the number : "))
x.append(a)
print(x)

xl = tuple(x)
print(xl)