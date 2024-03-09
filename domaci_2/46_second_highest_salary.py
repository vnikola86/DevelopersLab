def second_highest_salary(salaries):

    sorted_salaries = sorted(set(salaries), reverse=True)
    
    # Check if there are at least two unique salaries
    if len(sorted_salaries) >= 2:
        second_highest_salary = sorted_salaries[1]
        print(f"The salary of the employee with the second-highest income is: {second_highest_salary}")
    else:
        print("There must be at least two unique salaries in the list.")

user_input_salaries = [float(x) for x in input("Enter the list of employee salaries separated by space: ").split()]

second_highest_salary(user_input_salaries)
