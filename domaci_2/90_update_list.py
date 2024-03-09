def update_list(a, x):

    updated_list = [element + x if element % 2 == 0 else element for element in a]
    return updated_list

input_1 = [1, 2, -1, 3, -4]
input_2 = [21, 10, -10, 100]

x1 = 3
x2 = 5

output_1 = update_list(input_1, x1)
output_2 = update_list(input_2, x2)

print(f"Input 1: {input_1}, x = {x1}")
print(f"Updated list: {output_1}")

print(f"\nInput 2: {input_2}, x = {x2}")
print(f"Updated list: {output_2}")
