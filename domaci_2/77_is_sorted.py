def is_sorted_ascending(lst):

    return all(lst[i] <= lst[i+1] for i in range(len(lst)-1))

# Example usage:
user_input = input("Enter space-separated numbers: ")
numbers = [int(num) for num in user_input.split()]

result = is_sorted_ascending(numbers)
print(f"The list is sorted in ascending order: {result}")
