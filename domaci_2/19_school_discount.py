def calculate_school_fee(discount_criteria):

    school_fee, average_grade, has_award = discount_criteria

    discount_percentage = 0

    # Check for grade-based discounts
    if average_grade == 5.0:
        discount_percentage = 40
    elif average_grade >= 4.0:
        discount_percentage = 20
    elif average_grade >= 3.0:
        discount_percentage = 10

    # Check for award-based discount
    if has_award:
        discount_percentage = max(discount_percentage, 30)

    # Calculate the discounted fee
    discounted_fee = school_fee * (1 - discount_percentage / 100)

    # Round to the nearest integer
    return round(discounted_fee)

school_fee = float(input("Enter the school fee: "))
average_grade = float(input("Enter the average grade (2.0 to 5.0): "))
has_award = int(input("Does the student have an award? (0 for no, 1 for yes): "))

# Call the function and print the result
result = calculate_school_fee((school_fee, average_grade, has_award))
print(f"The student needs to pay: {result}")
