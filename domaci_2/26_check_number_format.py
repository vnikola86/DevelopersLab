def check_binary(number):

    return all(bit in '01' for bit in number)

def check_octal(number):

    return all(digit in '01234567' for digit in number)

def check_hexadecimal(number):

    return all(char.isdigit() or char.lower() in 'abcdef' for char in number)

def check_number_format(user_input):

    if user_input.startswith("0b"):
        if check_binary(user_input[2:]):
            return "Binary"
    elif user_input.startswith("0o"):
        if check_octal(user_input[2:]):
            return "Octal"
    elif user_input.startswith("0x"):
        if check_hexadecimal(user_input[2:]):
            return "Hexadecimal"
    else:
        try:
            int(user_input, 10)
            return "Decimal"
        except ValueError:
            pass

    return "Invalid"

user_input = input("Enter a number: ")

result = check_number_format(user_input)
print(f"The identified number format is: {result}")
