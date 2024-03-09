def square_and_sum(start, end):

    result_sum = sum(x**2 for x in range(start, end + 1) if x % 2 == 0 and x % 4 != 0)
    return result_sum

start_input = int(input("Enter the start of the range: "))
end_input = int(input("Enter the end of the range: "))

result_sum = square_and_sum(start_input, end_input)
print(f"The sum of squared values is: {result_sum}")
