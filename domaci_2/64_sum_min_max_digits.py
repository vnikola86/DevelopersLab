def sum_min_max_digits(number):
    # Convert the number to a string to iterate through its digits
    number_str = str(number)

    if len(number_str) == 0:
        return "Invalid input"

    # Initialize variables for min and max digits
    min_digit = 9  # set to the maximum possible digit initially
    max_digit = 0  # set to the minimum possible digit initially

    # Iterate through each digit in the number
    for digit_char in number_str:
        if digit_char.isdigit():
            digit = int(digit_char)
            min_digit = min(min_digit, digit)
            max_digit = max(max_digit, digit)

    # Calculate the sum of the min and max digits
    digit_sum = min_digit + max_digit

    return digit_sum

user_input = input("Enter a number: ")
try:
    user_number = int(user_input)
    result = sum_min_max_digits(user_number)
    print(f"The sum of the minimum and maximum digits is: {result}")
except ValueError:
    print("Invalid input. Please enter a valid number.")

