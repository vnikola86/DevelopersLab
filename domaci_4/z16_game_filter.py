import os

# Function to validate game attributes
def validate_game(game):
    name, rating, year, publisher, genres = game.split(';')
    
    if not (2 <= len(name) <= 50):
        return False
    try:
        rating = float(rating)
        if not (1 <= rating <= 10):
            return False
    except ValueError:
        return False
    try:
        year = int(year)
        if not (1950 < year < 2023):
            return False
    except ValueError:
        return False
    if publisher and not (2 <= len(publisher) <= 40):
        return False
    genres = genres.strip().split(' ')
    if len(genres) > 3:
        return False
    return True

# Function to get game genres
def get_genres():
    return ["Action", "Adventure", "Crime", "RPG", "Strategy", "Simulation"]

# Function to read games from file
def read_games(filename):
    games = []
    with open(filename, 'r') as file:
        for line in file:
            game = line.strip()
            if validate_game(game):
                games.append(game)
    return games

# Function to write games to file
def write_games(filename, games):
    with open(filename, 'w') as file:
        for game in games:
            file.write(game + '\n')

# Function to add new games
def add_games(filename):
    genres = get_genres()
    while True:
        name = input("Enter the name of the game: ")
        rating = input("Enter the rating of the game (1-10): ")
        year = input("Enter the release year of the game: ")
        publisher = input("Enter the publisher of the game (optional): ")
        print("Available genres:", genres)
        genres_input = input("Enter the genres of the game separated by space: ")
        game = f"{name};{rating};{year};{publisher};{genres_input}"
        if validate_game(game):
            with open(filename, 'a') as file:
                file.write(game + '\n')
            print("Game added successfully.")
        else:
            print("Invalid input. Please enter the game details again.")
        choice = input("Do you want to add another game? (yes/no): ")
        if choice.lower() != 'yes':
            break

# Function to filter games by attribute
def filter_games(games, attribute, value):
    filtered_games = []
    for game in games:
        attributes = game.split(';')
        if attribute == 'name':
            if attributes[0].startswith(value):
                filtered_games.append(game)
        elif attribute == 'rating':
            if float(attributes[1]) > float(value):
                filtered_games.append(game)
        elif attribute == 'year':
            if value.startswith('<'):
                if int(attributes[2]) < int(value[1:]):
                    filtered_games.append(game)
            elif value.startswith('>'):
                if int(attributes[2]) > int(value[1:]):
                    filtered_games.append(game)
        elif attribute == 'publisher':
            if attributes[3].startswith(value):
                filtered_games.append(game)
        elif attribute == 'genre':
            if value in attributes[4].split():
                filtered_games.append(game)
    return filtered_games

# Function to display games
def display_games(games):
    if not games:
        print("No games found.")
    else:
        print("Found games:")
        for game in games:
            print(game)

# Main function
def main():
    filename = "igrice.txt"
    genres = get_genres()
    if not os.path.exists(filename):
        print("File does not exist. Please create it with at least 10 games.")
        return
    
    games = read_games(filename)
    print("Games from file:")
    display_games(games)
    
    while True:
        choice = input("Do you want to add new games? (yes/no): ")
        if choice.lower() == 'yes':
            add_games(filename)
            games = read_games(filename)
            print("Updated games from file:")
            display_games(games)
        else:
            break
    
    attribute = input("Enter the attribute to filter by (name, rating, year, publisher, genre): ")
    value = input("Enter the value to filter by: ")
    filtered_games = filter_games(games, attribute.lower(), value)
    print("Filtered games:")
    display_games(filtered_games)

if __name__ == "__main__":
    main()
