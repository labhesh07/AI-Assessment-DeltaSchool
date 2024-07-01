
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
        return None

def calculator():
    print("Simple Calculator")
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
   
    operations = {
        '+': add,
        '-': subtract,
        '*': multiply,
        '/': divide
    }

    operation = input("Enter an operation (+, -, *, /): ").strip()

    if operation in operations:
        result = operations[operation](num1, num2)
        if result is not None:
            print(f"The result of {num1} {operation} {num2} is {result}.")
    else:
        print("Invalid operation. Please enter one of +, -, *, /.")

# Run the calculator
calculator()
