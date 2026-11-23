
def add(a, b):
    return a + b

#updated the substract code in branch1
def subtract(a,b):
    return a-b

# updated the multiply code in branch2
def multiply(a,b):
    return a*b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")

    return a / b
