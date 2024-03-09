def determine_quadrant(x, y):

    if x > 0 and y > 0:
        return "Quadrant I"
    elif x < 0 and y > 0:
        return "Quadrant II"
    elif x < 0 and y < 0:
        return "Quadrant III"
    elif x > 0 and y < 0:
        return "Quadrant IV"
    elif x == 0 and y != 0:
        return "On the y-axis"
    elif x != 0 and y == 0:
        return "On the x-axis"
    else:
        return "Origin (0,0)"

x_coordinate = float(input("Enter the x-coordinate of the point: "))
y_coordinate = float(input("Enter the y-coordinate of the point: "))

quadrant = determine_quadrant(x_coordinate, y_coordinate)
print(f"The point ({x_coordinate},{y_coordinate}) belongs to: {quadrant}")
