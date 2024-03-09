def count_art_grades(grades):

    grade_counts = {grade: 0 for grade in range(3, 6)}  # Assuming grades range from 3 to 5

    for grade in grades:
        if grade in grade_counts:
            grade_counts[grade] += 1

    return grade_counts

user_input_grades = [int(x) for x in input("Enter the list of art grades separated by space: ").split()]

result = count_art_grades(user_input_grades)
print("Number of students for each grade (excluding 1 and 2):")
for grade, count in result.items():
    print(f"Grade {grade}: {count} students")
