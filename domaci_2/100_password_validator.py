def check_password(input_string, min_string_len, flagUpper=False, flagLower=False, flagDigit=False):
    # Check if the string meets the minimum length requirement
    if len(input_string) < min_string_len:
        return False

    # Check for uppercase letters if required
    if flagUpper and not any(char.isupper() for char in input_string):
        return False

    # Check for lowercase letters if required
    if flagLower and not any(char.islower() for char in input_string):
        return False

    # Check for digits if required
    if flagDigit and not any(char.isdigit() for char in input_string):
        return False

    # If all checks pass, the password is valid
    return True

# Example
input_string = "Passw123"
min_length = 10
flag_upper = True
flag_lower = True
flag_digit = False

result = check_password(input_string, min_length, flag_upper, flag_lower, flag_digit)
print(result)
