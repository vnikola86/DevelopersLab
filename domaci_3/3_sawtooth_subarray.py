def longest_sawtooth_subarray(arr):
    max_length = 0
    max_subarray = []

    for i in range(len(arr) - 1):
        current_length = 1
        current_subarray = [arr[i]]

        # Check if the current subarray forms a sawtooth pattern
        for j in range(i, len(arr) - 1):
            if (j % 2 == 0 and arr[j] < arr[j + 1]) or (j % 2 != 0 and arr[j] > arr[j + 1]):
                current_length += 1
                current_subarray.append(arr[j + 1])
            else:
                break

        # Update the maximum length and subarray if necessary
        if current_length > max_length:
            max_length = current_length
            max_subarray = current_subarray

    return max_subarray

# Test the function
arr = [4, 5, 3, 4, 9, 8, 5, 6, 0, 1]
result = longest_sawtooth_subarray(arr)
print("Longest sawtooth subarray:", result)

