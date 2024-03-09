def encrypt_string(s):

    vowels = "aeiou"
    encrypted_string = ''.join('1' if char in vowels else '0' for char in s)
    return encrypted_string

user_input = input("Enter a string (lowercase alphabetic characters): ")

result = encrypt_string(user_input)
print(f"The encrypted string is: {result}")
