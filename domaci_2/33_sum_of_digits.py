def sum_of_digits(number):

    return sum(int(digit) for digit in str(abs(number)))

user_input = int(input("Enter a number: "))

result = sum_of_digits(user_input)
print(f"The sum of digits is: {result}")
