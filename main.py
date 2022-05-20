from operator import sub, add, mul, truediv


def calculator():

    print("Please enter the first and second number:")
    num1 = int(input('1st Number: '))
    num2 = int(input('2end Number: '))
    operators = {'+': add, '-': sub, '*': mul, '/': truediv}
    operator = input('Operator: ')
    print(operators.get(operator, invalid)(num1, num2))


def invalid():
    return "Invalid operator"


calculator()
