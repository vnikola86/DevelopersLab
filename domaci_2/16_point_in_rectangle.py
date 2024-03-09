def is_point_in_rectangle(point, rectangle_top_left, rectangle_bottom_right):

    point_x, point_y = point
    rect_top_left_x, rect_top_left_y = rectangle_top_left
    rect_bottom_right_x, rect_bottom_right_y = rectangle_bottom_right

    return rect_top_left_x <= point_x <= rect_bottom_right_x and \
           rect_top_left_y >= point_y >= rect_bottom_right_y

point_to_check = (3, 4)
rectangle_top_left = (2, 10)
rectangle_bottom_right = (7, 1)

if is_point_in_rectangle(point_to_check, rectangle_top_left, rectangle_bottom_right):
    print(f"The point {point_to_check} is inside the rectangle.")
else:
    print(f"The point {point_to_check} is outside the rectangle.")
