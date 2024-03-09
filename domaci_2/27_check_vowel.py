def contains_vowel(input_string):

    vowels = "aeiouAEIOU"

    for char in input_string:
        if char in vowels:
            return True

    return False

user_input = input("Enter a string: ")

result = contains_vowel(user_input)
if result:
    print("The string contains at least one vowel.")
else:
    print("The string does not contain any vowels.")
