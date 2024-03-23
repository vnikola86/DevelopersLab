# Function to check if a number ends with digit 3
def ends_with_3(number):
    return str(number)[-1] == '3'

# Initialize the sum
total_sum = 0

# Read data from the file
with open('hex_numbers.txt', 'r') as file:
    # Process each line in the file
    for line in file:
        # Strip leading and trailing whitespace
        line = line.strip()
        
        # Check if the line starts with '0x' (indicating a hexadecimal number)
        if line.startswith('0x'):
            # Extract the hexadecimal number and convert it to decimal (base 10)
            decimal_number = int(line, 16)
            
            # Check if the decimal number ends with digit 3
            if ends_with_3(decimal_number):
                # Add the number to the total sum
                total_sum += decimal_number

# Print the total sum
print("Total sum of numbers ending with 3:", total_sum)
