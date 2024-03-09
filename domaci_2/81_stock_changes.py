def analyze_stock_changes(stock_prices):

    if len(stock_prices) < 2:
        return "Insufficient data for analysis. Provide at least two stock prices."

    # Calculate price changes
    price_changes = [stock_prices[i + 1] - stock_prices[i] for i in range(len(stock_prices) - 1)]

    largest_increase = max(price_changes)
    largest_decrease = min(price_changes)

    return largest_increase, largest_decrease

user_input = input("Enter space-separated stock prices for the period: ")
stock_prices_list = [float(price) for price in user_input.split()]

result = analyze_stock_changes(stock_prices_list)
print(f"Largest increase: {result[0]}, Largest decrease: {result[1]}")
