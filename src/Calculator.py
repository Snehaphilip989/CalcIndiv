import math

def addition(x,y):
    return x+y 

def square(x):
    return  x*x

def subtraction(x,y):
    return y-x

def multiplication(x,y):
    return x*y

def division(x,y):
    return float(x)/float(y)

def squareroot(x):
    return  math.sqrt(x)



class Calculator:
    rest=0

    def __init__(self):
        pass

    def add(self, x, y):
        self.result = addition(x,y)
        return self.result


    def square(self,x):
        self.result = square(x)
        return self.result


    def subtract(self, x, y):
        self.result = subtraction(x,y)
        return self.result

    def multiply(self, x, y):
        self.result = multiplication(x,y)
        return self.result

    def divide(self, x, y):
        self.result = division(x,y)
        return self.result

    def root(self,x):
        self.result = squareroot(x)
        return self.result
