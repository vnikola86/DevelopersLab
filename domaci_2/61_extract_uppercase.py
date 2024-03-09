def extract_uppercase(text):
    uppercase_letters = [char for char in text if char.isupper()]
    return ''.join(uppercase_letters)

text = input("Enter a text: ")

result = extract_uppercase(text)
print(f"The uppercase letters in the text are: {result}")
