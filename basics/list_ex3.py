x = [1,2,3,5,2,6,2,4,5,6,8,7,51,6,4,8,4,8,4,4,2,3,6,8,7,3,2,2,1]

x_one = x.count(1)
x_two = x.count(2)
x_four = x.count(4)
x_five = x.count(5)

print('2,occurred',x_two,'time')
print('4,occurred',x_four,'time')
print('5,occurred',x_five,'time')

y = [25,45,6,2,21,22,32,23]
z = [1,3,3,5,6,1]

print('x adding y')
x.extend(y)
print(x)

