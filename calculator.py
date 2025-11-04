print("Welcome to Calculate 1.0\n")

x = int(input("Enter the value of x: "))
y = int(input("Enter the value of y: "))

oprtr = input("Enter operator (-, +, /, * ): ")

def calc(oprtr):
    match oprtr:
        case "+":
            print("The sum is ", x+y)
        case "-":
            print("The difference is ", x-y)
        case "*":
            print("The product is ", x*y)
        case "/":
            print("The quotient is ", x/y)
        case _:
            print("Error, Please enter the correct operator")

calc(oprtr)
