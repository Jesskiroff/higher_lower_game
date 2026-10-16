from game_data import data
import random


#bring data into program

def format_data(account):
    account_name = account["name"]
    account_description = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_description} from {account_country}."

def is_correct(users_guess, acc_a_followers, acc_b_followers):
    if acc_a_followers == acc_b_followers:
        return True
    if acc_a_followers > acc_b_followers:
        return users_guess == "a"
    else:
        return users_guess == "b"


score = 0
game_should_continue = True

#take data and make it usable
# make print statement out of data
#add input statemrnt for one to answer
account_a = random.choice(data)
account_b = random.choice(data)
if account_a == account_b:
    account_b == random.choice(data)


#create a while game_should_continue while loop
while game_should_continue:
    account_a = account_b
    account_b = random.choice(data)
    while account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)} ")
    print(f"To B: {format_data(account_b)} ")

    get_user_input = input(f"who has more followers: A or B?\n").lower()

    a_followers = account_a["follower_count"]
    b_followers = account_b["follower_count"]
    check_user_answer = is_correct(get_user_input, a_followers, b_followers)


    if check_user_answer:
        score += 1
        print(f"you're right! score is {score}")
    else:
        print(f"wrong, sorry. score is {score}")
        game_should_continue = False




#add score 