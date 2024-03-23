# Read dimensions of rectangles from the file
with open('rectangles.txt', 'r') as file:
    rectangles = [tuple(map(int, line.strip().split(','))) for line in file]

# Filter squares (where a = b)
squares = filter(lambda rect: rect[0] == rect[1], rectangles)

# Find the square with the largest area
largest_square = max(squares, key=lambda rect: rect[0] * rect[1])

# Calculate and print the area of the largest square
largest_area = largest_square[0] * largest_square[1]
print("Area of the largest square:", largest_area)
