def max_repeated_char(string):
    max_count = 0
    repeated_char = None

    for i in range(len(string) - 1):
        if string[i] == string[i + 1]:
            count = 1
            j = i + 1
            while j < len(string) - 1 and string[j] == string[j + 1]:
                count += 1
                j += 1

            if count > max_count:
                max_count = count
                repeated_char = string[i]

    return max_count + 1, repeated_char

# Test the function
string = "aabaaac"
result_count, result_character = max_repeated_char(string)
if result_character:
    print(f"The maximum repetition is {result_count} times, and the repeated character is '{result_character}'.")
else:
    print("There are no repeated neighbors in the given string.")


