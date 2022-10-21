class Calculator:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    # instance method
    def add(self):
        return self.x + self.y

    def subtract(self):
        return self.x - self.y

    def multiply(self):
        return self.x * self.y

    def divide(self):
        return self.x / self.y





from c3 import Calculator

task1 = Calculator(10, 20)
print(task1.add())
print(task1.multiply())
print(task1.divide())


task2 = Calculator(100, 200)
print(task2,add)
print(task2.subtract())
print(task2.multiply())
print(task2.divide())
