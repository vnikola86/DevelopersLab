import csv

def append_to_file(list_of_products):
    with open('products.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        # Write header if file is empty
        if file.tell() == 0:
            writer.writerow(["Naziv", "Opis", "Godina", "Kolicina", "Cijena"])
        # Write each product to the file
        for product in list_of_products:
            writer.writerow([product["naziv"], product["opis"], product["godina"], product["kolicina"], product["cijena"]])

def get_products_older_than(year):
    older_products = []
    with open('products.csv', 'r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if int(row["Godina"]) >= year:
                older_products.append(row)
    return older_products

def max_possible_revenue(products_list):
    revenue = 0
    for product in products_list:
        revenue += int(product["kolicina"]) * int(product["cijena"])
    return revenue

# Test the functions
if __name__ == "__main__":
    # Test data for append_to_file function
    products = [
        {"naziv": "Televizor", "opis": "LG televizor 43inc", "godina": 2019, "kolicina": 10, "cijena": 300},
        {"naziv": "Televizor", "opis": "Samsung televizor 39inc", "godina": 2017, "kolicina": 5, "cijena": 250}
    ]
    append_to_file(products)

    # Test data for get_products_older_than function
    older_products = get_products_older_than(2018)
    print("Products older than 2018:")
    for product in older_products:
        print(product)

    # Test data for max_possible_revenue function
    print("Max possible revenue:", max_possible_revenue(products))
