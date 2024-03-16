class CompanyCreationError(Exception):
    pass

class Company:
    def __init__(self, name, area, balance, max_num_of_employees):
        self._name = name
        self._area = area
        self._employees = []
        
        try:
            self._balance = self._validate_balance(balance)
            self._max_num_of_employees = self._validate_max_num_of_employees(max_num_of_employees)
        except ValueError as e:
            raise CompanyCreationError(e)

    def _validate_balance(self, balance):
        if balance < 0:
            raise ValueError("Balance cannot be negative.")
        return balance

    def _validate_max_num_of_employees(self, max_num_of_employees):
        if max_num_of_employees < 0:
            raise ValueError("Maximum number of employees cannot be negative.")
        return max_num_of_employees

    def add_employee(self, employee):
        if len(self._employees) < self._max_num_of_employees:
            self._employees.append(employee)
        else:
            print("Maximum number of employees reached. Cannot add more.")

    def remove_employee(self, employee_name, employee_surname):
        for employee in self._employees:
            if employee["name"] == employee_name and employee["surname"] == employee_surname:
                self._employees.remove(employee)
                return
        print("Employee not found.")

    def __str__(self):
        return f"name: {self._name}, area: {self._area}, balance: {self._balance}"

    def can_pay_employees(self):
        total_salary = sum(employee["salary"] for employee in self._employees)
        return total_salary <= self._balance

    def __gt__(self, other):
        return len(self._employees) > len(other._employees)


# Test the Company class
try:
    company1 = Company("Company A", "Technology", 10000, 5)
except CompanyCreationError as e:
    print(e)

try:
    company2 = Company("Company B", "Finance", 20000, 8)
except CompanyCreationError as e:
    print(e)

try:
    company3= Company("Company A", "Technology", -10000, 5)  # Invalid balance
except CompanyCreationError as e:
    print(e)

try:
    company4 = Company("Company B", "Finance", 20000, -8)    # Invalid max_num_of_employees
except CompanyCreationError as e:
    print(e)

print(company1) if 'company1' in locals() else print("Company 1 creation failed")
print(company2) if 'company2' in locals() else print("Company 2 creation failed")
print(company3) if 'company3' in locals() else print("Company 3 creation failed")
print(company4) if 'company4' in locals() else print("Company 4 creation failed")

company1.add_employee({"name": "John", "surname": "Doe", "salary": 5000})
company1.add_employee({"name": "Alice", "surname": "Smith", "salary": 4000})

print(f"Can Company 1 pay its employees? {company1.can_pay_employees()}")

company1.remove_employee("John", "Doe")
print(company1)

print(f"Does Company 1 have more employees than Company 2? {company1 > company2}")

