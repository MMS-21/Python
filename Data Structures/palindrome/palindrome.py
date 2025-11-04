"""Check if a given string is a palindrome using deque from collections module."""
from collections import deque
# A string is said to be a palindrome if the reverse of the string is the same as the string. 
# For example, “radar” is a palindrome, but “radix” is not a palindrome

def is_palindrome(string):
  # Create a deque to store the characters of the string
  deque_string = deque(string)

  # Iterate while the deque is not empty
  while len(deque_string) > 1:
    # Pop characters from both ends of the deque and compare them
    if deque_string.popleft() != deque_string.pop():
      return False

  # If the loop completes without returning False, the string is a palindrome
  return True

# Test Cases
strings = ["hello","radar"]
for string in strings:
    if is_palindrome(string):
        print(string, "is a palindrome.")
    else:
        print(string, "is not a palindrome.")