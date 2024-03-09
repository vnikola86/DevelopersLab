def is_bee_on_wire(x, y):

    expected_y = 2 * x + 5
    return y == expected_y

bee_x = 3.0
bee_y = 11.0

if is_bee_on_wire(bee_x, bee_y):
    print("The bee is moving along the wire.")
else:
    print("The bee is not on the wire.")