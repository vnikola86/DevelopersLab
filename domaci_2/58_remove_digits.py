def remove_digits(input_str):

    result = ""  # Initialize an empty string to store the result

    # Iterate through each character in the input string
    for char in input_str:
        # Check if the character is not a digit
        if not char.isdigit():
            result += char  # Append non-digit characters to the result string

    return result  # Return the result string

input_str = input("Enter the string containing letters, digits, and other characters: ")

result = remove_digits(input_str)
print(f"The new string without digits is: {result}")

