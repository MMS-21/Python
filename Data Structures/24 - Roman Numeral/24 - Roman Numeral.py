""" Module to convert Roman numerals to integers using the 'roman' module. """
from roman import fromRoman
# Convert Roman numeral to integer using the roman module
# Example Roman numeral
roman_numeral = "MCMXCIV"
# Convert to integer  
integer_value = fromRoman(roman_numeral)  

print(integer_value)