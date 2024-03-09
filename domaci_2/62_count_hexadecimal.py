def count_hexadecimal_numbers(s):
    words = s.split()
    count = 0

    for word in words:
        if word.startswith("0x") and all(c.isdigit() or c.lower() in 'abcdef' for c in word[2:]):
            count += 1

    return count

input_str = input("Enter a string: ")

result = count_hexadecimal_numbers(input_str)
print(f"The number of hexadecimal numbers in the string is: {result}")
