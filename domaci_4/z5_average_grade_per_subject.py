from functools import reduce

# Define the list of tuples containing student information (name, grade, subject)
student_data = [
    ("Ana", 9.5, "Math"),
    ("Marko", 8.8, "Math"),
    ("Jovan", 7.9, "Physics"),
    ("Milica", 9.2, "Physics"),
    ("Ivana", 8.7, "Math")
]

# Define the function to calculate the average grade per subject
def average_grade_per_subject(data):
    # Filter data for each subject
    filtered_data = {}
    for name, grade, subject in data:
        if subject not in filtered_data:
            filtered_data[subject] = []
        filtered_data[subject].append(grade)
    
    # Calculate the average grade for each subject
    averages = {}
    for subject, grades in filtered_data.items():
        averages[subject] = sum(grades) / len(grades)
    
    return averages

# Call the function and print the result
result = average_grade_per_subject(student_data)
print("Average grade per subject:", result)
