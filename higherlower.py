from game_data import data
import random

#create game that compares follower count from accounts in data
# get user input
#compare user input to right answer
# add score option
#if user gets answer right, score goes up
#if user gets answer wrong, game is over

def format_data(account):
    account_name = account["name"]
    account_description = account["description"]
    account_country =account ["country"]
    return f"{account_name}, a {account_description} from {account_country}"

def check_answer (user_guess, option_a, option_b):
    if option_a == option_b:
        return True
    if option_a > option_b:
        return user_guess == "a"
    else:
        return user_guess == "b"

account_a = random.choice(data)
account_b = random.choice(data)
while account_a == account_b:
    account_b = random.choice(data)

continue_game = True
score = 0

while continue_game:
    account_a = random.choice(data)
    account_b = random.choice(data)
    while account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A:{format_data(account_a)}")
    print(f"To B: {format_data(account_b)}")
    user_input = input(f"Who has more followers?").lower()

    account_a_followers = account_a["follower_count"]
    account_b_followers = account_b["follower_count"]
    right_answer = check_answer(user_input, account_a_followers, account_b_followers)

    if right_answer:
        score += 1
        print(f"You're right! Score is {score}")
    else:
        continue_game = False
        print(f"Game is over, your final score is {score}") 
