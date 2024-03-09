def check_neighbors(input_str, position):

    # Check if the position is within the valid range
    if 0 <= position < len(input_str):
        # Check if the current position and its neighbors are free
        if (position == 0 and input_str[position+1] == '0') or \
           (position == len(input_str)-1 and input_str[position-1] == '0') or \
           (input_str[position-1] == '0' and input_str[position+1] == '0'):
            return '1'
        else:
            return '0'
    else:
        return 'Error: Index is outside the valid range.'

input_str = input("Enter the string (consisting of 0s and 1s): ")
position = int(input("Enter the position to check (0-based index): "))

result = check_neighbors(input_str, position)
print(result)

