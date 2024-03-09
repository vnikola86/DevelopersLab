def adjust_salaries(salaries):
    # Calculate the average salary
    average_salary = sum(salaries) / len(salaries)

    # Adjust salaries based on the conditions
    adjusted_salaries = []
    for salary in salaries:
        if salary > average_salary:
            # Decrease salary by 10%
            adjusted_salaries.append(round(salary * 0.9, 2))
        else:
            # Increase salary by 10%
            adjusted_salaries.append(round(salary * 1.1, 2))

    adjusted_average_salary = sum(adjusted_salaries) / len (adjusted_salaries)

    return adjusted_salaries, sum(1 for salary in adjusted_salaries if salary > adjusted_average_salary)

# Read input from the user
try:
    # Assuming salaries are entered as space-separated values
    salaries = list(map(float, input("Enter salaries separated by spaces: ").split()))
except ValueError:
    print("Invalid input. Please enter valid numeric values.")
    exit()

adjusted_salaries, above_average_count = adjust_salaries(salaries)

print(f"Adjusted Salaries: {adjusted_salaries}")
print(f"The number of salaries above average after adjustment: {above_average_count}")
