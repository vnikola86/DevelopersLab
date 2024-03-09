def count_and_create_integer(text):

    digits = [char for char in text if char.isdigit()]
    digits_count = len(digits)
    result_integer = int(''.join(digits)) if digits_count > 0 else 0
    return digits_count, result_integer

user_input = input("Enter a text: ")

count_result, integer_result = count_and_create_integer(user_input)
print(f"Number of digits: {count_result}")
print(f"Integer created from digits: {integer_result}")
