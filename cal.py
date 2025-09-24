"""calculate"""

def adder_ab(a, b):
    '''a + b'''
    return print(a + b)

def main():
    '''
    txt -> operator
    a, b -> operand
    '''
    txt = input()
    a = int(input())
    b = int(input())
    result = "Sorry, I can't do this anymore...T_T"

    if txt == "+":
        result = adder_ab(a, b)

    print(result)

main()
