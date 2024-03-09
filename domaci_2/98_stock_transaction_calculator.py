def calculate_transaction_amount(quote):
    parts = quote.split()
    quantity = int(parts[1])
    price = float(parts[2])
    status = parts[3]

    if status == 'B':
        return quantity * price
    elif status == 'S':
        return -quantity * price
    else:
        return 0

def calculate_total_amount(quotes):
    buy_total = 0
    sell_total = 0

    for quote in quotes.split(','):
        transaction_amount = calculate_transaction_amount(quote)
        if transaction_amount > 0:
            buy_total += transaction_amount
        elif transaction_amount < 0:
            sell_total += abs(transaction_amount)

    return buy_total, sell_total

# Example
input_quotes = "ZNG 1300 2.66 B,NY 50 56.32 B,OWW 1000 11.623 B,OGG 20 580.1 B"

buy_total, sell_total = calculate_total_amount(input_quotes)

output_message = f"Buy: {buy_total:.2f} Sell: {sell_total:.2f}"
print(output_message)
