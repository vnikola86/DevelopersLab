def compare_apple_picking(p, m):
    if p > m:
        return "Petar je pobjednik!"
    else:
        return "Miloš je pobjednik!"


petar_apples = 15
milos_apples = 16

result_message = compare_apple_picking(petar_apples, milos_apples)
print(result_message)
