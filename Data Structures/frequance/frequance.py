"""Count the frequency of each word in a text file."""
from collections import Counter

# Define the function to count word frequencies
def word_frequency(filename):
    """Counts the occurrence of each word in a text file.

    Args:
        filename (str): The name of the text file.

    Returns:
        dict: A dictionary containing word frequencies.
    """
    try:
        # Open the file in read mode
        with open(filename, 'r') as file:
            # Read the file content and split into words
            words = file.read().lower().split()
            # Use Counter to count the occurrences of each word
            word_count = Counter(words)
    #handeling the Error of the not existed file
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        return {}
    # handling any other error
    except Exception as e:
        print(f"An error occurred: {e}")
        return {}
    # Return the dictionary containing word frequencies
    return dict(word_count)  

# I left a test file with the name test.txt
filename = "test.txt"  
word_frequency = word_frequency(filename)
# Print the word frequencies
print(word_frequency)  
