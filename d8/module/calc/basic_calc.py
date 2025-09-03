def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Division by zero error"
    return a / b

def module_name():
    print(f"My __name__ is {__name__}")

module_name()