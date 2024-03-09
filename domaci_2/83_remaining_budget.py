def remaining_budget(initial_budget, destination_prices):

    if not destination_prices:
        return "No destination prices provided. Please provide a list of prices."

    max_price = max(destination_prices)

    if initial_budget < max_price:
        return "Insufficient budget to afford the most expensive destination."

    remaining_amount = initial_budget - max_price
    return remaining_amount

user_input_budget = input("Enter your initial budget: ")
initial_budget = float(user_input_budget)

user_input_prices = input("Enter space-separated prices for each destination: ")
destination_prices_list = [float(price) for price in user_input_prices.split()]

result = remaining_budget(initial_budget, destination_prices_list)
print(f"The remaining budget after choosing the most expensive destination is: {result:.2f}")
