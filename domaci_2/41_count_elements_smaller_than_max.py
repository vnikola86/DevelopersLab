def count_elements_smaller_than_max(lst, max_value):

    count = sum(1 for num in lst if num < max_value)
    return count

user_input_list = [int(x) for x in input("Enter a list of integers separated by space: ").split()]
user_input_max = int(input("Enter the maximum value: "))

result = count_elements_smaller_than_max(user_input_list, user_input_max)
print(f"The number of elements smaller than {user_input_max} is: {result}")
