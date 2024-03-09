def enter_products(n):

    products = []

    for i in range(n):
        print(f"\nEnter information for Product {i + 1}:")
        name = input("Name: ")
        description = input("Description: ")
        price = float(input("Price: "))
        quantity = int(input("Quantity: "))

        product = {
            'name': name,
            'description': description,
            'price': price,
            'quantity': quantity
        }

        products.append(product)

    return products

def search_products(products, search_term):

    matching_products = [product for product in products if product['name'].startswith(search_term)]
    return matching_products


num_of_products = int(input("Enter the number of products: "))
all_products = enter_products(num_of_products)

search_term = input("\nEnter the search term for product names: ")
matching_products = search_products(all_products, search_term)

print("\nMatching Products:")
for product in matching_products:
    print(product)
