def count_elements_below_max(a, max_value):

    return sum(1 for element in a if element < max_value)

a_input = [int(x) for x in input("Enter elements for the list (comma-separated integers): ").split(',')]
max_input = int(input("Enter the maximum value: "))

result = count_elements_below_max(a_input, max_input)
print(f"The number of elements in the list below {max_input} is: {result}")
