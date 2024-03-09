def filter_games_by_rating_and_publisher(games, rating_threshold, publisher_name):

    filtered_games = [
        game for game in games
        if game['ocjena'] >= rating_threshold and game['izdavac'].lower() == publisher_name.lower()
    ]
    return filtered_games

# Example
games_list = [
    {'ime': 'Game1', 'izdavac': 'Publisher1', 'godina_izlaska': 2020, 'ocjena': 8.5},
    {'ime': 'Game2', 'izdavac': 'Publisher2', 'godina_izlaska': 2021, 'ocjena': 9.0},
    {'ime': 'Game3', 'izdavac': 'Publisher1', 'godina_izlaska': 2019, 'ocjena': 7.5},
]

rating_threshold = float(input("Enter the minimum rating: "))
publisher_name = input("Enter the publisher name: ")

filtered_games = filter_games_by_rating_and_publisher(games_list, rating_threshold, publisher_name)

print("\nFiltered Games:")
for game in filtered_games:
    print(game)
