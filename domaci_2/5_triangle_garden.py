def is_valid_triangle(side1, side2, side3):

  return side1 + side2 > side3 and side1 + side3 > side2 and side2 + side3 > side1

side1_length = 5
side2_length = 7
side3_length = 10

if is_valid_triangle(side1_length, side2_length, side3_length):
  print("A garden in the shape of a triangle can be created with these side lengths.")
else:
  print("It's not possible to create a garden in the shape of a triangle with these side lengths.")
