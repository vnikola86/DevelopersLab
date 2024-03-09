def replace_element(input_list, old_element, new_element):
    replaced_list = [new_element if item == old_element else item for item in input_list]
    return replaced_list

# Read input from the user
try:
    input_list = input("Enter a list of integers (space-separated): ")
    input_list = [int(item) for item in input_list.split()]
    old_element = int(input("Enter the element to replace: "))
    new_element = int(input("Enter the new element: "))
except ValueError:
    print("Invalid input. Please enter valid integers.")
    exit()

result_list = replace_element(input_list, old_element, new_element)
print(f"The list after replacing {old_element} with {new_element} is: {result_list}")
