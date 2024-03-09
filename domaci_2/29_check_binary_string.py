def is_binary_string(input_string):

    return all(char in "01" for char in input_string)

user_input = input("Enter a string: ")

result = is_binary_string(user_input)
if result:
    print("The entered string is a binary number.")
else:
    print("The entered string is not a binary number.")
