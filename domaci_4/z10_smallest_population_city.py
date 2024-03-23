# Read data from the file
with open('population.txt', 'r') as file:
    lines = file.readlines()

# Initialize a dictionary to store the smallest population of each country
smallest_populations = {}

# Process each line in the file
for line in lines:
    country, city, population = line.strip().split(',')
    population = int(population)
    # Convert the country name to lowercase
    country = country.lower()
    # Check if the country already exists in smallest_populations
    if country in smallest_populations:
        # If the population is smaller than the current minimum, update it
        if population < smallest_populations[country][1]:
            smallest_populations[country] = (city, population)
    else:
        # If the country doesn't exist, add it to the dictionary
        smallest_populations[country] = (city, population)

# Get the input country from the user and convert it to lowercase
input_country = input("Enter the country name: ").strip().lower()

# Check if the input country exists in the smallest_populations dictionary
if input_country in smallest_populations:
    # Retrieve the city with the smallest population for the input country
    smallest_city = smallest_populations[input_country][0]
    print(f"The city with the smallest population in {input_country.capitalize()} is '{smallest_city}'")  # Capitalize the country name for output
else:
    print("Country not found in the file.")

