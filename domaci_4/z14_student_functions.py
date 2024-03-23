def append_to_file(list_of_students):
    with open('students.txt', 'a') as file:
        for student in list_of_students:
            file.write(f"{student['ime']},{student['prezime']},{student['godina']},{student['prosjek']}\n")

def get_students_with_greater_grade(year, grade):
    grade_range = {
        'A': (9.5, 10),
        'B': (8.5, 9.5),
        'C': (7.5, 8.5),
        'D': (6.5, 7.5),
        'E': (6, 6.5)
    }

    selected_students = []
    lower_bound, upper_bound = grade_range[grade]

    with open('students.txt', 'r') as file:
        for line in file:
            ime, prezime, godina, prosjek = line.strip().split(',')
            godina = int(godina)
            prosjek = float(prosjek)
            if godina == year and lower_bound <= prosjek < upper_bound:
                selected_students.append({
                    'ime': ime,
                    'prezime': prezime,
                    'godina': godina,
                    'prosjek': prosjek
                })

    return selected_students

# Testing the functions
if __name__ == "__main__":
    # Test data for append_to_file function
    students_data = [
        {"ime": "Marko", "prezime": "Markovic", "godina": 2, "prosjek": 8.6},
        {"ime": "Boris", "prezime": "Boricic", "godina": 3, "prosjek": 7.9},
        {"ime": "Novak", "prezime": "Novovic", "godina": 3, "prosjek": 6.9}
    ]
    append_to_file(students_data)

    # Test data for get_students_with_greater_grade function
    selected_students = get_students_with_greater_grade(3, 'C')
    print("Students with grade greater than or equal to C:")
    for student in selected_students:
        print(student)
