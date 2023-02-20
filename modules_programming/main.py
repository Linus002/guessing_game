# import operators module
import operator

import others

# get numbers

operator = input("Enter operator:")
if operator == "cube":
    num = eval(input("Enter number:"))
    x = others.cube(num)
    print(x)

else:

    num1 = eval(input("Enter number 1:"))
    num2 = eval(input("Enter number 2:"))

    if operator == "+":
        x = operator.add(num1, num2)
        print(x)

    elif operator == "-":
        x =  operator.subtract(num1, num2)
        print(x)

    elif operator == "/":
        x = operator.divide(num1, num2)
        print(x)

    elif operator == "*" or "x" or "X":
        x = operator.multiply(num1, num2)
        print(x)

