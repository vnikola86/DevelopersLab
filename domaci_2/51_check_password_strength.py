def is_strong_password(password):

    # Check if the password meets the criteria
    has_lowercase = any(char.islower() for char in password)
    has_uppercase = any(char.isupper() for char in password)
    has_digit = any(char.isdigit() for char in password)
    is_length_valid = len(password) >= 8

    # Return the result
    return "YES" if has_lowercase and has_uppercase and has_digit and is_length_valid else "NO"

user_password = input("Enter a password: ")

result = is_strong_password(user_password)
print(f"Is the password strong? {result}")
