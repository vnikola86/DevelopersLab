def encrypt_string(s):
    encrypted_str = ""
    
    for char in s:
        if char.isdigit():
            if int(char) % 2 == 0:
                encrypted_str += '0'
            else:
                encrypted_str += '1'
        else:
            encrypted_str += char

    return encrypted_str

input_str = input("Enter a string of digits (0-9): ")
result = encrypt_string(input_str)
print(f"The encrypted string is: {result}")
