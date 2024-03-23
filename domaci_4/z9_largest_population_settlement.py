# Read data from the file
with open('cities.txt', 'r') as file:
    lines = file.readlines()

# Initialize a dictionary to store the population of each settlement
populations = {}

# Process each line in the file
for line in lines:
    city, settlement, population = line.strip().split(',')
    population = int(population)
    # Convert the city name to lowercase
    city = city.lower()
    if city in populations:
        if populations[city][1] < population:
            populations[city] = (settlement, population)
    else:
        populations[city] = (settlement, population)

# Get the settlement with the highest population for the input city
input_city = input("Enter the city name: ").strip().lower()  # Convert input to lowercase
if input_city in populations:
    largest_settlement = populations[input_city][0]
    print(f"The settlement with the largest population in {input_city.capitalize()} is '{largest_settlement}'")  # Capitalize the city name for output
else:
    print("City not found in the file.")
