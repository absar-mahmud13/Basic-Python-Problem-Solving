# module.py

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

class Calculator:
    def __init__(self, value=0):
        self.value = value

    def add(self, number):
        self.value += number
        return self.value

    def subtract(self, number):
        self.value -= number
        return self.value

    def get_value(self):
        return self.value
