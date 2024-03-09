def intersection(a, b):

    return [item for item in a if item in b]

a_input = input("Enter elements for list a (comma-separated): ").split(',')
b_input = input("Enter elements for list b (comma-separated): ").split(',')

result = intersection(a_input, b_input)
print(f"The intersection of lists a and b is: {result}")
