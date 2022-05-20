from operator import sub, add, mul, truediv


def calculator():
    print("""
    + - Addition
    - - Subtraction
    * - Multiplication
    / - Division
    """)
    print("Please enter the first number:")
    num1 = int(input(':'))
    print("Please enter the operator:")
    operator = input(':')
    print("Please enter the second number:")
    num2 = int(input(':'))
    operators = {'+': add, '-': sub, '*': mul, '/': truediv}

    if operator in operators:
        print(operators[operator](num1, num2))
    else:
        print("Invalid operator")


calculator()
