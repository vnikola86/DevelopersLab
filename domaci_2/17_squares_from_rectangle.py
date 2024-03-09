def can_create_squares(rectangle_width, rectangle_height):

    # Check if the rectangle can be split into two squares with side lengths equal to the smaller dimension
    if rectangle_width >= 2 * rectangle_height or rectangle_height >= 2 * rectangle_width:
        return True

    return False

rectangle_width = 8
rectangle_height = 4

if can_create_squares(rectangle_width, rectangle_height):
    print(f"At least two squares can be created from the rectangle with dimensions {rectangle_width}x{rectangle_height}.")
else:
    print(f"Two squares cannot be created from the rectangle with dimensions {rectangle_width}x{rectangle_height}.")
