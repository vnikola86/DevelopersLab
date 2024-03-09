def calculate_digit_sum_product(number):

    if number % 2 == 0:  # If the number is even
        even_digit_sum = sum(int(digit) for digit in str(number) if int(digit) % 2 == 0)
        return even_digit_sum
    else:  # If the number is odd
        odd_digit_product = 1
        for digit in str(number):
            if int(digit) % 2 != 0:
                odd_digit_product *= int(digit)
        return odd_digit_product

user_input = int(input("Enter a four-digit number: "))

# Check if the input is a four-digit number
if 1000 <= user_input <= 9999:
    result = calculate_digit_sum_product(user_input)
    print(f"The result is: {result}")
else:
    print("Invalid input. Please enter a four-digit number.")
