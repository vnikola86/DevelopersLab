class Drzava:
    def __init__(self, name, population):
        self._name = name
        self._population = population
        self._border = []
        self._cities = []

    def get_name(self):
        return self._name

    def get_population(self):
        return self._population

    def get_border(self):
        return self._border

    def set_population(self, population):
        self._population = population

    def add_to_border(self, country):
        self._border.append(country)

    def add_city(self, city, population):
        self._cities.append({"name": city, "population": population})

    def print_largest_city(self):
        largest_city = max(self._cities, key=lambda x: x["population"])
        print(f"Largest city in {self._name}: {largest_city['name']} ({largest_city['population']} population)")

    def print_smallest_city(self):
        smallest_city = min(self._cities, key=lambda x: x["population"])
        print(f"Smallest city in {self._name}: {smallest_city['name']} ({smallest_city['population']} population)")

    def __str__(self):
        cities_info = "; ".join([f"{city['name']} ({city['population']})" for city in self._cities])
        return f"Country: {self._name}, Population: {self._population}, Cities: {cities_info}"


class Federacija(Drzava):
    def __init__(self, name, population):
        super().__init__(name, population)
        self._countries = []

    def get_countries(self):
        return self._countries

    def set_countries(self, countries):
        self._countries = countries

    def __lt__(self, other_federation):
        return len(self._countries) < len(other_federation.get_countries())

    def __gt__(self, other_federation):
        return len(self._countries) > len(other_federation.get_countries())

    def __str__(self):
        countries_info = "; ".join(self._countries)
        return f"Federation: {self.get_name()}, Number of countries: {len(self._countries)}, Countries: {countries_info}"


# Test the classes
country1 = Drzava("Country1", 1000000)
country1.add_city("City1", 500000)
country1.add_city("City2", 200000)
country1.print_largest_city()
country1.print_smallest_city()
print(country1)

country2 = Drzava("Country2", 2000000)
country2.add_city("City3", 800000)
country2.add_city("City4", 300000)
country2.print_largest_city()
country2.print_smallest_city()
print(country2)

country3 = Drzava("country3", 3000000)
country3.add_city("City5", 1000000)
country3.add_city("City6", 500000)
country3.print_largest_city()
country3.print_smallest_city()
print(country3)

country4 = Drzava("country4", 4000000)
country4.add_city("City7", 2000000)
country4.add_city("City8", 100000)
country4.print_largest_city()
country4.print_smallest_city()
print(country4)

country5 = Drzava("country5", 5000000)
country5.add_city("City9", 2500000)
country5.add_city("City10", 200000)
country5.print_largest_city()
country5.print_smallest_city()
print(country5)

federation1 = Federacija("Federation1", 3000000)
federation1.add_to_border("Country3")
federation1.add_to_border("Country4")
federation1.set_countries(["Country1", "Country2"])
print(federation1)

federation2 = Federacija("Federation2", 12000000)
federation2.add_to_border("Country1")
federation2.add_to_border("Country2")
federation2.set_countries(["Country3", "Country4", "Country5"])
print(federation2)

# Testing comparison
print("Is federation1 smaller than federation2?", federation1 < federation2)
print("Is federation1 larger than federation2?", federation1 > federation2)
