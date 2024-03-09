def reserve_rows_for_group(seat_counts_per_row, group_size):

    if not seat_counts_per_row:
        return "No seat counts provided. Please provide a list of seat counts per row."

    seat_counts_per_row.sort(reverse=True)  # Sort rows in descending order of seat count

    total_seats = 0
    rows_needed = 0

    for seats_in_row in seat_counts_per_row:
        total_seats += seats_in_row
        rows_needed += 1

        if total_seats >= group_size:
            break

    return rows_needed

user_input_seat_counts = input("Enter space-separated seat counts per row: ")
seat_counts_list = [int(seat_count) for seat_count in user_input_seat_counts.split()]

user_input_group_size = input("Enter the size of the visiting group: ")
group_size = int(user_input_group_size)

result = reserve_rows_for_group(seat_counts_list, group_size)
print(f"The minimum number of rows needed is: {result}")
