def above_average_employees(salaries):

    average_salary = sum(salaries) / len(salaries)
    above_average_count = sum(1 for salary in salaries if salary > average_salary)

    print(f"The number of employees with salaries above the average is: {above_average_count}")

user_input_salaries = [float(x) for x in input("Enter the list of employee salaries separated by space: ").split()]

above_average_employees(user_input_salaries)
