""" A program to determine if a number is even or odd using bitwise operations. """
def even_or_odd(num):
    # Check the last bit to determine if the number is even or odd
    print(f"{num} is even." if num & 1 == 0 else f"{num} is odd.")
# Reading the number from the STDN 
num = int(input("Enter a numeber: "))
even_or_odd(num)