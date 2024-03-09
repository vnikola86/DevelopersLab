def add_prefix_suffix(a, pre, suf, num):

    result = pre * num + a + suf * num
    return result

# Input: The user enters the values for a, pre, suf, and num
a = input("Enter the string (a): ")
pre = input("Enter the prefix (pre): ")
suf = input("Enter the suffix (suf): ")
num = int(input("Enter the number of times to add the prefix and suffix (num): "))

result = add_prefix_suffix(a, pre, suf, num)
print(f"The resulting string is: {result}")
