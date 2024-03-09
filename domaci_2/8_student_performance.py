def determine_student_performance(average):

    if average >= 4.5:
        return "Odličan"
    elif 3.5 <= average < 4.5:
        return "Vrlo dobar"
    elif 2.5 <= average < 3.5:
        return "Dobar"
    elif 2 <= average < 2.5:
        return "Dovoljan"
    else:
        return "Nedovoljan"

student_average = 4.5

performance_level = determine_student_performance(student_average)
print(f"Student's performance level: {performance_level}")
