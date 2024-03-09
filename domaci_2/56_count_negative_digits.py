def count_single_digit_negatives(input_str):

    # Separate the input string using '-' as a separator
    segments = input_str.split('-')

    # Count the number of single-digit negative numbers
    count = 0

    for segment in segments:
        # Check if the segment starts with '+', and skip it
        if segment.startswith('+'):
            continue

        # Check if the segment has length 1 (single-digit negative number)
        if len(segment) == 1:
            count += 1

        else:
            # Split the segment using '+' as a separator and consider the first part
            negative_segment = segment.split('+')[0]

            # Check if the first part is a single-digit negative number
            if int(negative_segment) < 10:
                count += 1

    return count

input_str = input("Enter the string of positive/negative numbers: ")

result = count_single_digit_negatives(input_str)

print(f"The number of single-digit negative numbers is: {result}")


