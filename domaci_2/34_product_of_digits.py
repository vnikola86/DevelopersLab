def product_of_digits(text):

    digits = [int(char) for char in text if char.isdigit()]
    product = 1 if digits else 0  # Initialize product to 1 if there are digits, else 0
    for digit in digits:
        product *= digit
    return product

user_input = input("Enter a text: ")

result = product_of_digits(user_input)
print(f"The product of digits is: {result}")
