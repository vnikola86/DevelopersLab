def count_occurrences(numbers_list, target_number):
    return numbers_list.count(target_number)

# Read input from the user
try:
    numbers_list = input("Enter a list of numbers separated by spaces: ").split()
    target_number = int(input("Enter the number to count: "))
    numbers_list = list(map(int, numbers_list))
except ValueError:
    print("Invalid input. Please enter valid numbers.")
    exit()

result = count_occurrences(numbers_list, target_number)

print(f"The number {target_number} occurs {result} times in the list.")
