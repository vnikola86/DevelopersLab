def sum_of_squares_divisible_by_three(numbers):
    # Calculate the sum of squares for elements divisible by 3
    result = sum(x**2 for x in numbers if x % 3 == 0)
    return result

# Read input from the user
try:
    # Assuming numbers are entered as space-separated values
    numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
except ValueError:
    print("Invalid input. Please enter valid integer numeric values.")
    exit()

result = sum_of_squares_divisible_by_three(numbers)

print(f"The sum of squares of elements divisible by 3 is: {result}")
