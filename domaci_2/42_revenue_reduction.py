def calculate_revenue_reduction(original_prices, reduction_percentage):

    original_revenue = sum(original_prices)
    reduced_prices = [price - price * (reduction_percentage / 100) for price in original_prices]
    reduced_revenue = sum(reduced_prices)
    reduction_amount = original_revenue - reduced_revenue
    return reduction_amount

user_input_prices = [float(x) for x in input("Enter the list of original product prices separated by space: ").split()]
user_input_percentage = float(input("Enter the reduction percentage: "))

result = calculate_revenue_reduction(user_input_prices, user_input_percentage)
print(f"The reduction in revenue is: {result:.2f}")
