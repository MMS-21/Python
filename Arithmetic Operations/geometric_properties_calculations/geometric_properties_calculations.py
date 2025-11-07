""" A program to calculate the area of a rectangle and the circumference of a circle. """
# importing the math library to be able to use pi 
import math

# Reading the length and width of the rectangle from the STDN
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

# Calculating the area of the rectangle
area = length * width

# Print the calculated area of the rectangle
print(f"The area of the rectangle is: {area}")

# Reading the radius of the circle from the STDN
radius = float(input("Enter the radius of the circle: "))

# Calculating the circumference of the circle
circumference = 2 * math.pi * radius

# Print the calculated circumference
print(f"The circumference of the circle is: {circumference}")