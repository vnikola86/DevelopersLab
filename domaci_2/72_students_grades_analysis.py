def count_students_above_average(grades):
    # Remove grades of 5 from the list
    filtered_grades = [grade for grade in grades if grade < 5]

    # Calculate the average grade
    average_grade = sum(filtered_grades) / len(filtered_grades) if filtered_grades else 0

    # Count students with grades above the average
    count_above_average = sum(1 for grade in filtered_grades if grade > average_grade)

    return count_above_average

# Example
grades = [4, 5, 3, 4, 5, 2, 4]
result = count_students_above_average(grades)
print(f"The number of students with grades above the average is: {result}")
