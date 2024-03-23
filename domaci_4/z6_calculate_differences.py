# Define the time series array
time_series = [10, 15, 30, 50, 75]

# Define the function to calculate the difference between consecutive pairs
def calculate_difference(series):

    differences = list(map(lambda x, y: y - x, series[:-1], series[1:]))
    return differences

# Call the function and print the result
result = calculate_difference(time_series)
print("Differences between consecutive pairs:", result)
