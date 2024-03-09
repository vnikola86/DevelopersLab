def longest_increasing(input_list):
    current_sublist = []
    max_sublist = []

    for num in input_list:
        if num > 0:
            if not current_sublist or num > current_sublist[-1]:
                current_sublist.append(num)
            else:
                if len(current_sublist) > len(max_sublist):
                    max_sublist = current_sublist
                current_sublist = [num]
        else:
            if len(current_sublist) > len(max_sublist):
                max_sublist = current_sublist
            current_sublist = []

    # Check if the last sublist is the longest
    if len(current_sublist) > len(max_sublist):
        max_sublist = current_sublist

    return max_sublist

# Example
original_list = [1, 2, 3, -1, 0, 5, 6, 7, 10, 10, 1]

print(f"Original list: {original_list}")

result = longest_increasing(original_list)

print(f"The longest ascending subarray of positive integers in the provided list: {result}")


