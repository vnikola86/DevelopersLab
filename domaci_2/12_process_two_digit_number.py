def process_two_digit_number(number):

    if not (10 <= number <= 99):
        return "Invalid input. Please provide a two-digit number."

    first_digit = number // 10
    second_digit = number % 10

    if first_digit > second_digit:
        return first_digit - second_digit
    elif first_digit < second_digit:
        return first_digit + second_digit
    else:
        return first_digit * second_digit


two_digit_number = 23

result = process_two_digit_number(two_digit_number)
print(f"The result for the two-digit number {two_digit_number} is: {result}")
