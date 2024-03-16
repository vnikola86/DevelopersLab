class Student:
    def __init__(self, name, surname, year):
        self._name = name
        self._surname = surname
        self._subjects = []
        self.set_year(year)

    def get_name(self):
        return self._name

    def get_surname(self):
        return self._surname

    def get_year(self):
        return self._year

    def set_year(self, year):
        if 0 < year <= 8:
            self._year = year
        else:
            print("Invalid year value. Year must be between 1 and 8.")

    def insert_subject(self, subject):
        self._subjects.append(subject)

    def remove_subject(self, subject_name):
        self._subjects = [s for s in self._subjects if s["naziv"] != subject_name]

    def compute_average(self):
        total_credits = 0
        total_grade_points = 0

        for subject in self._subjects:
            grade = subject["ocjena"]
            credits = subject["broj_kredita"]
            if grade != "F":
                total_credits += credits
                if grade == "A":
                    total_grade_points += 10 * credits
                elif grade == "B":
                    total_grade_points += 9 * credits
                elif grade == "C":
                    total_grade_points += 8 * credits
                elif grade == "D":
                    total_grade_points += 7 * credits
                elif grade == "E":
                    total_grade_points += 6 * credits

        if total_credits != 0:
            return total_grade_points / total_credits
        else:
            return 0  # If no subjects or all subjects have F grade

    def __str__(self):
        average = self.compute_average()
        return f"\"ime\": \"{self._name}\", \"prezime\": \"{self._surname}\", \"prosjek\": {average:.2f}"

# Test the class
student1 = Student("John", "Doe", 3)
student1.insert_subject({"naziv": "Matematika", "ocjena": "A", "broj_kredita": 6})
student1.insert_subject({"naziv": "Fizika", "ocjena": "B", "broj_kredita": 4})

student2 = Student("Jane", "Smith", 2)
student2.insert_subject({"naziv": "Istorija", "ocjena": "C", "broj_kredita": 5})
student2.insert_subject({"naziv": "Hemija", "ocjena": "D", "broj_kredita": 3})

print("Student 1:", student1)
print("Student 2:", student2)

student1.set_year(4)
print(f"{student1.get_name()} {student1.get_surname()} je učenik {student1.get_year()}. razreda.")

student1.remove_subject("Fizika")
print("Student 1:", student1)