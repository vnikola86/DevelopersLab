def validate_credit_card(card_number):
    # Check if the card number contains only digits and has length 16
    if not card_number.isdigit() or len(card_number) != 16:
        return False

    # Convert the card number to a list of integers
    card_digits = [int(digit) for digit in card_number]

    # Double every second digit from the right
    for i in range(15, -1, -2):
        card_digits[i] *= 2
        if card_digits[i] > 9:
            card_digits[i] = card_digits[i] // 10 + card_digits[i] % 10

    # Check if the sum of digits is divisible by 10
    return sum(card_digits) % 10 == 0

def validate_credit_cards_in_file(input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            card_number = line.strip()
            if validate_credit_card(card_number):
                outfile.write(card_number + ',Valid\n')
            else:
                outfile.write(card_number + ',Invalid\n')

# Test the functions
if __name__ == "__main__":
    # Test the credit card validation function
    print("Credit card validation:")
    print("12345:", validate_credit_card("12345"))
    print("1234567890123456:", validate_credit_card("1234567890123456"))
    print("891:", validate_credit_card("891"))

    # Test the function to validate credit cards in a file
    validate_credit_cards_in_file("cc_info.txt", "validated_credit_cards.txt")
