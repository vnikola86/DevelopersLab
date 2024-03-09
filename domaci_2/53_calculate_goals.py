def calculate_goals(petros_sum):

    goals = 0  # Initialize the number of goals
    current_sum = 0  # Initialize the current sum of goals

    # Iterate until the current sum exceeds or equals Petro's sum
    while current_sum <= petros_sum:
        # Increment the number of goals
        goals += 1
        # Update the current sum based on the new goal
        current_sum += goals

    return goals - 1  # Decrement by 1 to get the correct number of goals

petros_sum = int(input("Enter Petro's sum: "))

result = calculate_goals(petros_sum)
print(f"The number of goals is: {result}")

