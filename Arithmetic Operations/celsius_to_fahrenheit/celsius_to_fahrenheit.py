"""
This program reads a user's temperature in Celsius or Fahrenheit from standard input (STDIN) and then converts it to the other temperature.
"""
# Reading The Type of the Temperature from STDIN
choice = input("Convert from Celsius (C) or Fahrenheit (F)? Enter C or F: ").upper()
# Conditional Statements to handle the choice    
if choice == "C":
    # Reading The Celsius Temperature from STDIN
    celsius = float(input("Enter temperature in Celsius: "))
    # Conveting the celsius to Fahrenheit
    fahrenheit = (celsius * 9/5) + 32
    # Printing the results out
    print(f"{celsius}°C is {fahrenheit}°F")
elif choice == "F":
    # Reading The Fahrenheit Temperature from STDIN
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    # Conveting the Fahrenheit to celsius
    celsius = (fahrenheit - 32) * 5/9
    # Printing the results out
    print(f"{fahrenheit}°F is {celsius}°C")
else:
    # Handling any other input
    print("Invalid input!")