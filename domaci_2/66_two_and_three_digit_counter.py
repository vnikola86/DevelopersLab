def count_two_and_three_digit_numbers(number_list):
    count_two_digit = 0
    count_three_digit = 0

    for num in number_list:
        if 10 <= abs(num) <= 99:
            count_two_digit += 1
        elif 100 <= abs(num) <= 999:
            count_three_digit += 1

    return count_two_digit, count_three_digit

try:
    numbers = [int(x) for x in input("Enter a list of integers separated by spaces: ").split()]
except ValueError:
    print("Invalid input. Please enter valid integers.")
    exit()

two_digit, three_digit = count_two_and_three_digit_numbers(numbers)

if two_digit > three_digit:
    print("There are more two-digit numbers than three-digit numbers.")
elif three_digit > two_digit:
    print("There are more three-digit numbers than two-digit numbers.")
else:
    print("The number of two-digit and three-digit numbers is equal.")
