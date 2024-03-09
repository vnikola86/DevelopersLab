import math

def calculate_circumference_and_area(radius):

    circumference = 2 * math.pi * radius
    area = math.pi * radius**2
    return circumference, area

radius_table1 = 5.0
radius_table2 = 7.0

circumference_table1, area_table1 = calculate_circumference_and_area(radius_table1)
circumference_table2, area_table2 = calculate_circumference_and_area(radius_table2)

if area_table1 > area_table2:
    print(f"The circumference of the table with a larger area is: {round(circumference_table1, 2)}")
else:
    print(f"The circumference of the table with a larger area is: {round(circumference_table2, 2)}")