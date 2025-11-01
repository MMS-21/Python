"""This script creates a dictionary of the first 10 prime numbers and their squares"""
## The sympy function needs to be installed
from sympy import isprime
# Start checking numbers from 2 (the first prime number)
# Initialize an empty dictionary to store prime numbers and their squares
prime_squares = {}

# Counter to keep track of how many primes we've found
counter = 0

num = 0

# Loop until we find the first 10 prime numbers
while counter < 10:
    # Check if the number is prime
    if isprime(num):  
        # Map the prime to its square
        prime_squares[num] = num ** 2  
        # Increment the prime counter
        counter += 1  
    # Move to the next number
    num += 1  

# Print the resulting dictionary
print(prime_squares)