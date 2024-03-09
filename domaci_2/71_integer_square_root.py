def count_integer_square_roots(numbers):
    count = 0

    for number in numbers:
        square_root = number ** 0.5
        if square_root % 1 == 0:
            count += 1

    return count

try:
    input_numbers = list(map(int, input("Enter a list of numbers separated by space: ").split()))
except ValueError:
    print("Invalid input. Please enter valid numbers.")
    exit()

result = count_integer_square_roots(input_numbers)
print(f"The total number of integers with integer square roots in the list is: {result}")
