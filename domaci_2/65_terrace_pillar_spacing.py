def calculate_distances(terrace_length, num_pillars, pillar_width):

    if num_pillars < 1:
        print("Invalid input. Number of pillars should be greater than or equal to 1.")
        exit()

    # Convert pillar width to meters
    pillar_width_meters = pillar_width / 100

    # Calculate the distance between pillars
    distance_between_pillars = (terrace_length - num_pillars * pillar_width_meters) / (num_pillars + 1)

    return distance_between_pillars*100

# Read input from the user
try:
    terrace_length = float(input("Enter the length of the terrace in meters: "))
    num_pillars = int(input("Enter the number of pillars: "))
    pillar_width = float(input("Enter the width of a pillar in centimeters: "))
except ValueError:
    print("Invalid input. Please enter valid numbers.")
    exit()

dist_between_pillars = calculate_distances(terrace_length, num_pillars, pillar_width)

print(f"The distance between pillars, as well as between pillars and the wall, is: {dist_between_pillars:.2f} centimeters")
