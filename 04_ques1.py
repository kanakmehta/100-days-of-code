# Write a program to swap two numbers without using a third variable.

def swap(a, b):
    a, b = b, a
    return a, b
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
print(num1, num2)
num1, num2 = swap(num1, num2)
print("After swapping: ")
print(num1, num2)