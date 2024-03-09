def sum_and_count_divisible(a, b, divisor):

    sum_divisible = sum(x for x in range(a + 1, b) if x % divisor == 0)
    count_divisible = sum(1 for x in range(a + 1, b) if x % divisor == 0)
    return sum_divisible, count_divisible

a_input = int(input("Enter the start of the range (exclusive): "))
b_input = int(input("Enter the end of the range (exclusive): "))
divisor_input = int(input("Enter the divisor: "))

sum_result, count_result = sum_and_count_divisible(a_input, b_input, divisor_input)

print(f"The sum of elements divisible by {divisor_input} is: {sum_result}")
print(f"The count of elements divisible by {divisor_input} is: {count_result}")
