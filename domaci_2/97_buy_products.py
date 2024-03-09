def input_products(num_products):
    products = []
    for _ in range(num_products):
        product = {
            'naziv': input("Unesite naziv proizvoda: "),
            'opis': input("Unesite opis proizvoda: "),
            'cijena': float(input("Unesite cijenu proizvoda: ")),
            'broj_artikala': int(input("Unesite broj dostupnih artikala: "))
        }
        products.append(product)
    return products

def calculate_max_products(products, product_name, available_money):
    for product in products:
        if product['naziv'] == product_name:
            return min(product['broj_artikala'], int(available_money / product['cijena']))
    return 0

num_products = int(input("Unesite broj proizvoda: "))
all_products = input_products(num_products)

searched_product = input("Unesite naziv proizvoda koji želite kupiti: ")
available_money = float(input("Unesite iznos novca koji imate na raspolaganju: "))

max_products_to_buy = calculate_max_products(all_products, searched_product, available_money)

print(f"Možete kupiti najviše {max_products_to_buy} komada proizvoda '{searched_product}'.")
