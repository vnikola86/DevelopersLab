def calculate_power(base, exponent):

    result = 1.0

    for _ in range(abs(exponent)):
        result *= base if exponent > 0 else 1 / base

    return result

user_input = input("Enter the base and exponent separated by space: ").split()
base, exponent = map(float, user_input)

result = calculate_power(base, int(exponent))
print(f"{base} raised to the power of {exponent} is: {result}")
