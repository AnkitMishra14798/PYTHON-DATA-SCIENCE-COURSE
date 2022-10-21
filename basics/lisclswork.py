names = []
for i in range(5):
    names.append(input("name=>"))
for name in names:
    print(name[::-1])

# fibonacci

fib = [0,1]
for i in range(15):
    fib.append( fib[-1] + fib[-2])
print(fib)

# squrers

x = [1,2,3,4,5,6,7,8,9,10]
x2 = []
for num in x:
    x2.append(num ** 2)
print(x)
print(x2)

# find odd number in the given list

x = [1,2,3,4,5,6,7,8,9,10]

xodd = []
for i in x:
    if i % 2 !=0:
        xodd.append(i)
print(xodd)

# find even number in the given list

x = [1,2,3,4,5,6,7,8,9,10]

xeven = []
for i in x:
    if i % 2==0:
        xeven.append(i)
print(xeven)


