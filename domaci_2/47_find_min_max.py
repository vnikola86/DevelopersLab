def find_min_max(num1, num2, num3):

    minimum = min(num1, num2, num3)
    maximum = max(num1, num2, num3)
    print(f"The minimum among the three numbers is: {minimum}")
    print(f"The maximum among the three numbers is: {maximum}")

user_input = input("Enter three numbers separated by space: ").split()
user_input_num1, user_input_num2, user_input_num3 = map(float, user_input)

find_min_max(user_input_num1, user_input_num2, user_input_num3)

