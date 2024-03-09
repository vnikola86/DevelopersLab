def count_opposite_elements(a):

    unique_elements = set(a)
    count = sum(1 for element in unique_elements if -element in unique_elements)
    return count

input_1 = [1, 2, -1, 3, -3]
input_2 = [20, 10, -10, 100]

output_1 = count_opposite_elements(input_1)
output_2 = count_opposite_elements(input_2)

print(f"Example 1: {input_1}")
print(f"The number of elements with their opposites in the list is: {output_1}")

print(f"\nExample 2: {input_2}")
print(f"The number of elements with their opposites in the list is: {output_2}")
