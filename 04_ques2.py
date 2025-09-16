# Write a program to find and display the sum of the first n natural numbers.
def sum_natural(n):
    for i in range(1, n+1):
        sum = n*(n+1)/2
    return sum
num = int(input("Enter a number: "))
print("The sum of first", num, "natural numbers is:", sum_natural(num))