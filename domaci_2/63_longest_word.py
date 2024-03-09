import re

def longest_word(input_str):
    # Remove special characters and split the string into words
    words = re.sub(r'[^A-Za-z0-9\s]', '', input_str).split()

    if not words:
        return None  # Empty string case

    longest = max(words, key=len)
    return longest

# Input: User enters a string
input_str = input("Enter a string: ")

# Output: Longest word in the given string
result = longest_word(input_str)
print(f"The longest word in the string is: {result}")
