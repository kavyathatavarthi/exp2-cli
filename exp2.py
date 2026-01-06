print("Collaborative Calculator Application")
print("Addition operator")
# Simple Addition Program
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

result = num1 + num2

print("Sum =", result)
# Simple Subtraction Program

result = num1 - num2

print("Difference =", result)
# Simple Multiplication Program


result = num1 * num2

print("Product =", result)
# Simple Division Program


if num2 != 0:
    result = num1 / num2
    print("Quotient =", result)
else:
    print("Error: Division by zero is not allowed")

