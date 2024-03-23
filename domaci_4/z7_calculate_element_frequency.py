from functools import reduce

# Define the list
fruits = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']

# Define the function to calculate the frequency of each element
def calculate_frequency(lst):
    # Map each element to a dictionary with initial count 1
    mapped = map(lambda x: {x: 1}, lst)
    # Reduce to merge dictionaries and sum up counts for each element
    frequencies = reduce(lambda x, y: {k: x.get(k, 0) + y.get(k, 0) for k in set(x) | set(y)}, mapped)
    return frequencies

# Call the function and print the result
result = calculate_frequency(fruits)
print("Frequency of each element:", result)
