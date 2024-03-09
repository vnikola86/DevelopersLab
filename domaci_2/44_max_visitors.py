def max_visitors_in_one_day(visitors_list):

    max_visitors = max(visitors_list)
    print(f"The maximum number of visitors in one day was: {max_visitors}")

user_input_visitors = [int(x) for x in input("Enter the list of visitors for the last ten football matches separated by space: ").split()]

max_visitors_in_one_day(user_input_visitors)
