"""This script removes duplicates from a list by converting it to a set"""
# A list of numbers
numbers = [1, 5, 3, 1, 5, 1, 5, 1, 5, 9, 2]


def drop_duplicates(numbers):
    # Converting the list to a set
    new_numbers_set = set(numbers)

    # printing the new numbers set
    print(new_numbers_set)

if __name__ == "__main__":
    drop_duplicates(numbers)