def square_and_sum(start, end):
    total_sum = 0
    
    for num in range(start, end + 1):
        if num % 3 == 0 and num % 6 != 0:
            total_sum += num ** 2
    
    return total_sum

start = int(input("Enter the start of the segment: "))
end = int(input("Enter the end of the segment: "))

result = square_and_sum(start, end)
print(f"The sum of squares of numbers divisible by 3 but not by 6 is: {result}")
