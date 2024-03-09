def split_string(input_str, number):
    result = []
    current_substring = ""

    for char in input_str:
        current_substring += char

        if len(current_substring) == number:
            result.append(current_substring)
            current_substring = ""

    # Check if the last substring needs padding
    if current_substring:
        current_substring += '*' * (number - len(current_substring))
        result.append(current_substring)

    return result

# Example
input_str1 = "danas polažemo test"
input_str2 = "kurs web program."
input_str3 = "da"

number1 = 5
number2 = 6
number3 = 7

result1 = split_string(input_str1, number1)
result2 = split_string(input_str2, number2)
result3 = split_string(input_str3, number3)

print(f"Input: '{input_str1}', Number: {number1} -> Result: {result1}")
print(f"Input: '{input_str2}', Number: {number2} -> Result: {result2}")
print(f"Input: '{input_str3}', Number: {number3} -> Result: {result3}")
