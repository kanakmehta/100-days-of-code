# Write a program to input two numbers and display their sum, difference, product, and quotient.
print("Enter two numbers:")
num1 = float(input("enter first no:"))
num2 = float(input("enter second no:"))
sum = num1 + num2
print(sum)
difference = num1 - num2
print(difference)
product = num1 * num2
print(product)
quotient = num1 / num2
if num2 == 0:
    print("undefined")
else:
    print(quotient)
