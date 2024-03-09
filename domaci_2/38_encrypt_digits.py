def encrypt_digits(s):

    encrypted_string = ''.join('0' if int(char) % 2 == 0 else '1' for char in s if char.isdigit())
    return encrypted_string

user_input = input("Enter a string (containing digits): ")

result = encrypt_digits(user_input)
print(f"The encrypted string is: {result}")
