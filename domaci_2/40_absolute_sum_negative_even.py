def absolute_sum_negative_even(numbers):

    abs_sum = sum(abs(num) for num in numbers if num < 0 and num % 2 == 0)
    return abs_sum

user_input = [int(x) for x in input("Enter a list of integers separated by space: ").split()]

result = absolute_sum_negative_even(user_input)
print(f"The absolute sum of negative even elements is: {result}")
