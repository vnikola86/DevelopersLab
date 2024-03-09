def second_highest_price(products):

    if len(products) < 2:
        return "Not enough products to determine the second highest price."

    # Remove duplicates and sort in descending order
    unique_prices = sorted(set(products), reverse=True)

    return unique_prices[1]

user_input = input("Enter space-separated product prices: ")
prices = [float(price) for price in user_input.split()]

result = second_highest_price(prices)
print(f"The value of the second most expensive product is: {result}")
