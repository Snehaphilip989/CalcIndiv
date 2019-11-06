import math

def addition(x,y):
    return x+y


class Calculator:
    rest=0

    def __init__(self):
        pass

    def add(self, x, y):
        self.result = addition(x,y)
        return self.result