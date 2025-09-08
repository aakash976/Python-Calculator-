# Python Calculator Project

import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

def modulus(x, y):
    return x % y

def power(x, y):
    return x ** y

def square_root(x):
    return math.sqrt(x)

def calculator():
    while True:
        print("\n===== PYTHON CALCULATOR =====")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Modulus")
        print("6. Power (x^y)")
        print("7. Square Root")
        print("8. Exit")

        choice = input("Enter choice (1-8): ")

        if choice == "8":
            print("Exiting... Thank you for using Calculator!")
            break

        if choice == "7":
            num = float(input("Enter number: "))
            print("Result:", square_root(num))

        elif choice in ["1", "2", "3", "4", "5", "6"]:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == "1":
                print("Result:", add(num1, num2))
            elif choice == "2":
                print("Result:", subtract(num1, num2))
            elif choice == "3":
                print("Result:", multiply(num1, num2))
            elif choice == "4":
                print("Result:", divide(num1, num2))
            elif choice == "5":
                print("Result:", modulus(num1, num2))
            elif choice == "6":
                print("Result:", power(num1, num2))
        else:
            print("Invalid Input! Please enter a number between 1-8.")

# Run the calculator
calculator()