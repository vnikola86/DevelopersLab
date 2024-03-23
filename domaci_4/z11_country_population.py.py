# Read data from the file
with open('population.txt', 'r') as file:
    lines = file.readlines()

# Initialize a dictionary to store the total population of each country
total_populations = {}

# Process each line in the file
for line in lines:
    country, _, population = line.strip().split(',')
    population = int(population)
    # Check if the country already exists in total_populations
    if country in total_populations:
        # If the country exists, add the population to the total
        total_populations[country] += population
    else:
        # If the country doesn't exist, initialize the total with population
        total_populations[country] = population

# Get the input country from the user
input_country = input("Enter the country name: ").strip()

# Convert the input country to lowercase
input_country = input_country.lower()

# Find the total population for the input country
total_population = total_populations.get(input_country.capitalize(), None)

# Print the total population for the input country
if total_population is not None:
    print(f"The total population of {input_country.capitalize()} is {total_population}")
else:
    print("Country not found in the file.")

