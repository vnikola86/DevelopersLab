def determine_winner(math_points1, programming_points1, math_points2, programming_points2):

    total_points1 = math_points1 + programming_points1
    total_points2 = math_points2 + programming_points2

    if total_points1 > total_points2 or (total_points1 == total_points2 and programming_points1 > programming_points2):
        return "Competitor 1"
    elif total_points2 > total_points1 or (total_points1 == total_points2 and programming_points2 > programming_points1):
        return "Competitor 2"
    else:
        return "It's a tie!"

math_points_competitor1 = 40
programming_points_competitor1 = 30

math_points_competitor2 = 35
programming_points_competitor2 = 35

winner = determine_winner(math_points_competitor1, programming_points_competitor1,
                           math_points_competitor2, programming_points_competitor2)

print(f"The winner is: {winner}")
