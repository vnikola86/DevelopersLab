def calculate_sum_and_product(n):

    sum_even = 0
    product_odd = 1
    count_even = 0
    count_odd = 0

    for i in range(1, n + 1):
        if i % 2 == 0:
            sum_even += i
            count_even += 1
        else:
            product_odd *= i
            count_odd += 1

    return sum_even, product_odd, count_even, count_odd

user_input = int(input("Enter a number (n): "))

sum_even, product_odd, count_even, count_odd = calculate_sum_and_product(user_input)

print(f"Sum of even numbers: {sum_even}")
print(f"Product of odd numbers: {product_odd}")
print(f"Count of even numbers: {count_even}")
print(f"Count of odd numbers: {count_odd}")
