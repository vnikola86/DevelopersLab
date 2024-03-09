def shorten_string(input_string, desired_length):

    if desired_length < len(input_string):
        return input_string[:desired_length] + '...'
    else:
        return input_string + '...'

user_input = input("Enter the string and desired length separated by space: ").split()
input_string, desired_length = user_input[0], int(user_input[1])

result = shorten_string(input_string, desired_length)
print(f"The shortened string is: {result}")
