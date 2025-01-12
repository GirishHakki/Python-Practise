import re


def linear_search(lst, pattern):
    # Compile the pattern using re
    regex = re.compile(pattern)

    # Iterate over the list and check if the pattern matches any element
    for index, element in enumerate(lst):
        if regex.search(element):
            return f"Pattern found in element '{element}' at index {index}"

    return "Pattern not found in the list"


# Example list
my_list = ["apple", "banana", "cherry", "date", "elderberry"]

# Pattern to search for
pattern = "an"  # Searching for the substring 'an'

# Perform linear search
result = linear_search(my_list, pattern)

# Output the result
print(result)