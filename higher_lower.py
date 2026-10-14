#display the welcome message
#from art import logo
from game_data import data
import random
#

def format_data(account):
    account_name = account["name"]
    account_description = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_description}, from {account_country} "

def check_answer(user_guess, a_followers, b_followers):
    if a_followers == b_followers:
        return True
    if a_followers > b_followers:
        return user_guess == "a"
    return user_guess == "b"

score = 0
game_should_continue = True

#generate a random account from the data
account_a = random.choice(data)
account_b = random.choice(data)
if account_a== account_b:
    account_b = random.choice(data)


while game_should_continue:

    account_a = account_b
    account_b = random.choice(data)
    while account_a == account_b:
        account_b = random.choice(data)
#format account data into printable format 
    print(f"Compare A: {format_data(account_a)}. ")
    print(f"Against B: {format_data(account_b)}. ")
    #ask user for guess

    guess = input("who has more followers? Type 'A' or 'B: ").lower()
    #check if user is correct

    # - get follower count of each accoiunt
    follower_count_a = account_a["follower_count"]
    follower_count_b = account_b["follower_count"]
    is_correct = check_answer(guess, follower_count_a, follower_count_b)
    # use if statement to chck if user is correct

    #give user feedback on their guess

#score keeping
    if is_correct:
        score += 1
        print(f"You're right! Current score {score}")
    else:
        print(f"Sorry, that's wrong. Your score is {score}!")
        game_should_continue = False




