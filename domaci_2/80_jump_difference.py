def jump_difference(jump_lengths):

    if not jump_lengths:
        return "List of jump lengths is empty."

    min_jump = min(jump_lengths)
    max_jump = max(jump_lengths)

    return max_jump - min_jump

user_input = input("Enter space-separated jump lengths in centimeters: ")
jump_lengths_list = [int(length) for length in user_input.split()]

result = jump_difference(jump_lengths_list)
print(f"The difference between the longest and shortest jumps is: {result} cm")
