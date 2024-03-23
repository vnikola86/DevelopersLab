students = [
    {'ime': 'Ana', 'godine': 22, 'prosek': 9.1},
    {'ime': 'Marko', 'godine': 20, 'prosek': 8.5},
    {'ime': 'Jovan', 'godine': 23, 'prosek': 9.8},
    {'ime': 'Milica', 'godine': 21, 'prosek': 8.9}
]


def filter_and_sort(students):
    filtered_students = filter(lambda x: x['godine'] > 21, students)
    sorted_students = sorted(filtered_students, key=lambda x: x['prosek'], reverse=True)
    return sorted_students


result = filter_and_sort(students)
print("Filtered and sorted students older than 21:", result)
