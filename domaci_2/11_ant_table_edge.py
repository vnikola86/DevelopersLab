def is_ant_on_table_edge(ant_coordinates, table_top_right, table_bottom_left):
    
    ant_x, ant_y = ant_coordinates
    table_right, table_top = table_top_right
    table_left, table_bottom = table_bottom_left

    return (table_left <= ant_x <= table_right and ant_y == table_bottom) or \
           (table_bottom <= ant_y <= table_top and ant_x == table_left) or \
           (table_left <= ant_x <= table_right and ant_y == table_top) or \
           (table_bottom <= ant_y <= table_top and ant_x == table_right)

ant_coordinates = (2, 4)
table_top_right = (8, 6)
table_bottom_left = (2, 1)

if is_ant_on_table_edge(ant_coordinates, table_top_right, table_bottom_left):
    print("The ant is moving along the edge of the table.")
else:
    print("The ant is not on the table edge.")
