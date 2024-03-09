def find_min_price_pair(product_prices):

    min_total_price = float('inf')
    min_price_pair = None
    min_price_products = None

    for i in range(len(product_prices)):
        for j in range(i + 1, len(product_prices)):
            total_price = product_prices[i] + product_prices[j]

            if total_price < min_total_price:
                min_total_price = total_price
                min_price_pair = (i, j)
                min_price_products = (product_prices[i], product_prices[j])

    return (min_price_pair, min_price_products)

product_prices = [15.99, 9.99, 5.99]

min_price_indices, min_price_values = find_min_price_pair(product_prices)

if min_price_indices is not None:
    product1, product2 = min_price_indices
    value1, value2 = min_price_values
    print(f"The pair of products with the smallest total price is: Product{product1 + 1} ({value1}) and Product{product2 + 1} ({value2})")
else:
    print("No valid pair found.")
