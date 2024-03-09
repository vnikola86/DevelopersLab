def extract_vowels(input_string):

    vowels = "aeiouAEIOU"
    result = ''.join(char for char in input_string if char in vowels)
    return result

user_input = input("Enter a string: ")

result = extract_vowels(user_input)
print(f"The string containing only vowels is: {result}")
