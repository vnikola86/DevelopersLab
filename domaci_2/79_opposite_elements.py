def count_opposite_elements(numbers):

    opposite_count = 0
    unique_numbers = set(numbers)

    for num in unique_numbers:
        if -num in unique_numbers:
            opposite_count += 1

    return int(opposite_count/2)

user_input = input("Enter space-separated integers (without zero): ")
numbers_list = [int(num) for num in user_input.split()]

result = count_opposite_elements(numbers_list)
print(f"The number of elements with opposite values is: {result}")
