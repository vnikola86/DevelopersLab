def increase_above_average(salaries, increase_amount):
    # Calculate the average salary
    average_salary = sum(salaries) / len(salaries)

    # Increase salaries above the average by the specified amount
    increased_salaries = [salary + increase_amount if salary > average_salary else salary for salary in salaries]

    return increased_salaries

# Read input from the user
try:
    salaries = input("Enter a list of salaries separated by spaces: ").split()
    increase_amount = float(input("Enter the amount to increase salaries above the average: "))
    salaries = list(map(float, salaries))
except ValueError:
    print("Invalid input. Please enter valid numbers.")
    exit()

result = increase_above_average(salaries, increase_amount)

print(f"The salaries after increasing those above the average by {increase_amount} euros are: {result}")
