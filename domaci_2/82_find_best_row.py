def find_best_row(seat_counts, group_size):

    if group_size <= 0:
        return "Invalid group size. Please enter a positive integer."

    if not seat_counts:
        return "No data available. Provide a list of seat counts."

    if group_size > max(seat_counts):
        return "Group size exceeds the maximum available seats in any row."

    # Calculate remaining seats after accommodating the group in each row
    remaining_seats = [seats - group_size for seats in seat_counts]

    # Find the row with the maximum remaining seats
    best_row_index = remaining_seats.index(max(remaining_seats))

    return best_row_index + 1

user_input_seats = input("Enter space-separated seat counts for each row: ")
seat_counts_list = [int(seats) for seats in user_input_seats.split()]

user_input_group_size = input("Enter the group size: ")
group_size = int(user_input_group_size)

result = find_best_row(seat_counts_list, group_size)
print(f"The best row for the group is row {result}")
