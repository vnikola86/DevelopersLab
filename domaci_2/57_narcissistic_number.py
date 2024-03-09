def is_narcissistic_number(number):

    num_str = str(number)
    num_digits = len(num_str)
    narcissistic_sum = sum(int(digit)**num_digits for digit in num_str)

    if narcissistic_sum == number:
        return "jeste"
    else:
        return "nije"

user_input = int(input("Unesite broj: "))

result = is_narcissistic_number(user_input)
print(f"Dati broj {result} 'narcissistic number'")