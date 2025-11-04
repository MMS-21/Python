""" Module to calculate the Levenshtein distance between two strings. """
import Levenshtein  
# Calculate the Levenshtein distance between two strings.
def calculate_levenshtein_distance(str1, str2):

    distance = Levenshtein.distance(str1, str2)
    return distance


# Example String
string1 = "kitten"  
string2 = "sitting" 

# Calculate the Levenshtein distance
levenshtein_dist = calculate_levenshtein_distance(string1, string2)
# Print the result
print(f"The Levenshtein distance between '{string1}' and '{string2}' is: {levenshtein_dist}")
