students = ["Marko", "Ana", "Jovan", "Milica"]
grades = [8.9, 7.5, 9.2, 8.8]


def high_grades(students, grades):
    return list(filter(lambda x: x[1] > 8.5, zip(students, grades)))


result = high_grades(students, grades)
print("Students with average grade above 8.5:", result)
