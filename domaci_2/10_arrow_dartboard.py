import math

def is_arrow_hitting_dartboard(arrow_coordinates, dartboard_center, dartboard_radius):

    arrow_x, arrow_y = arrow_coordinates
    dartboard_center_x, dartboard_center_y = dartboard_center

    distance = math.sqrt((arrow_x - dartboard_center_x)**2 + (arrow_y - dartboard_center_y)**2)

    return distance <= dartboard_radius

# Example
arrow_coordinates = (3, 4)
dartboard_center = (2, 3)
dartboard_radius = 1.5

if is_arrow_hitting_dartboard(arrow_coordinates, dartboard_center, dartboard_radius):
    print("The arrow is hitting the dartboard.")
else:
    print("The arrow is not hitting the dartboard.")
