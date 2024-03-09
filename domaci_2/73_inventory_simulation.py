def get_item_from_inventory(inventory, position):
    # Check if the position is valid
    if 0 <= position < len(inventory):
        print(f"The item at position {position} in the inventory is: {inventory[position]}")
    else:
        print("Error: Invalid position in the inventory.")

# Example inventory
player_inventory = ["sword", "hat", "gloves", "shield", "potion"]

# Read input from the user
try:
    position = int(input(f"Enter the position in the inventory (0 to {len(player_inventory) - 1}): "))
except ValueError:
    print("Invalid input. Please enter a valid position.")
    exit()

get_item_from_inventory(player_inventory, position)

