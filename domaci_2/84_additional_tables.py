def additional_tables_needed(guests, table_capacities):

    if not table_capacities:
        return "No table capacities provided. Please provide a list of capacities."

    total_seating_capacity = sum(table_capacities)
    additional_guests = max(0, guests - total_seating_capacity)

    # Each additional table provides 4 seats
    additional_tables_needed = (additional_guests + 3) // 4

    return additional_tables_needed

user_input_guests = input("Enter the number of guests: ")
guests = int(user_input_guests)

user_input_capacities = input("Enter space-separated table capacities: ")
table_capacities_list = [int(capacity) for capacity in user_input_capacities.split()]

result = additional_tables_needed(guests, table_capacities_list)
print(f"The number of additional tables needed is: {result}")
