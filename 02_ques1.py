# Write a program to calculate the area and perimeter of a rectangle given its length and breadth.
print("Enter the length of the rectangle:")
length = float(input())
print("Enter the breadth of the rectangle:")
breadth = float(input())
area = length * breadth
perimeter = 2 * (length + breadth)
print(f"area is {area}")
print(f"perimeter is {perimeter}")