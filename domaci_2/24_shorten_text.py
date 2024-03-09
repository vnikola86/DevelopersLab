def shorten_text(text):

    if len(text) > 30:
        shortened_text = text[:27] + '…'
    else:
        shortened_text = text

    return shortened_text

user_input = input("Enter a text: ")

result = shorten_text(user_input)
print(f"The shortened text is: {result}")
