import random

def calculate_score(text):

    score = sum(1 if char == '1' else 0 if char == '0' else -1 for char in text)
    return score

def check_player_status():

    choices = ['10010*', '0*1*010', '*010110', '1101*', '0*1*01*']
    random_choice = random.choice(choices)

    player_score = calculate_score(random_choice)

    if player_score > 0:
        return f"Card selected: '{random_choice}'. Player is in plus with a score of {player_score}."
    elif player_score == 0:
        return f"Card selected: '{random_choice}'. Player has a neutral score (zero)."
    else:
        return f"Card selected: '{random_choice}'. Player is in minus with a score of {player_score}."

result_message = check_player_status()
print(result_message)
