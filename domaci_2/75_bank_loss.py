def calculate_total_loss(savings_list, interest_rate):
    total_loss = 0

    for savings in savings_list:
        interest = savings * (interest_rate / 100)
        total_loss += interest

    return total_loss

# Read input from the user
try:
    savings_input = input("Enter the initial savings amounts (space-separated): ")
    savings_list = [float(amount) for amount in savings_input.split()]
    interest_rate = float(input("Enter the fixed interest rate on savings in percentage: "))
except ValueError:
    print("Invalid input. Please enter valid numbers.")
    exit()

total_loss = calculate_total_loss(savings_list, interest_rate)
print(f"The total loss from interest after the given period is: {total_loss:.2f}")
