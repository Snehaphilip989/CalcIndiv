import math

def addition(x,y):
    return x+y

def subtraction(x,y):
    return y-x


class Calculator:
    rest=0

    def __init__(self):
        pass

    def add(self, x, y):
        self.result = addition(x,y)
        return self.result


    def subtract(self, x, y):
        self.result = subtraction(x,y)
        return self.result
