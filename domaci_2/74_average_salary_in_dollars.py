def calculate_average_salary_in_dollars(salaries_in_euros):
    exchange_rate = 1.1
    salaries_in_dollars = [salary * exchange_rate for salary in salaries_in_euros]
    average_salary_in_dollars = sum(salaries_in_dollars) / len(salaries_in_dollars)
    return average_salary_in_dollars

try:
    salaries_in_euros = [float(salary) for salary in input("Enter salaries in euros (space-separated): ").split()]
except ValueError:
    print("Invalid input. Please enter valid numbers.")
    exit()

average_salary_in_dollars = calculate_average_salary_in_dollars(salaries_in_euros)

print(f"The average salary in dollars is: {average_salary_in_dollars:.2f} USD (1 euro = 1.10 USD)")
