def absolute_of_even_sum(numbers):

    even_sum = 0

    for num in numbers:
        if num < 0 and num % 2 == 0:
            even_sum += abs(num)

    return even_sum

user_input_numbers = input("Enter space-separated integers: ")
numbers_list = [int(number) for number in user_input_numbers.split()]

result = absolute_of_even_sum(numbers_list)
print(f"The absolute sum of negative even elements is: {result}")
