def remove_first_last_char(text):

    if len(text) >= 2:
        modified_text = text[1:-1]
    else:
        modified_text = text

    return modified_text

user_input = input("Enter a text: ")

result = remove_first_last_char(user_input)
print(f"The modified text is: {result}")
