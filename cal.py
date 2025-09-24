"""calculate"""

def adder(a, b):
    '''a + b'''
    return a + b

def subtract(a, b):
    """a - b"""
    return a - b

def multiply(a, b):
    """a x b"""
    return a * b

def devide(a, b):
    """a / b"""
    return a / b

def main():
    '''
    txt -> operator
    a, b -> operand
    '''
    txt = input()
    a = int(input())
    b = int(input())
    result = "Sorry, I can't do this anymore...T_T"

    match txt:
        case "+":
            result = adder(a, b)
        case "-":
            result = subtract(a, b)
        case "*":
            result = multiply(a, b)
        case "/":
            result = devide(a, b)

    print(result)

main()
