from game_data import data
import random


#bring data into program

def format_data(account):
    account_name = account["name"]
    account_description = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_description} from {account_country}."


#take data and make it usable
# make print statement out of data
#add input statemrnt for one to answer


account_a = random.choice(data)
account_b = random.choice(data)
if account_a == account_b:
    account_b == random.choice(data)

score = 0
game_should_continue = True

get_user_input = input(f"who has more followers: A or B?\n").lower()

#create a while game_should_continue while loop


while game_should_continue:
    account_a = account_b
    account_b = random.choice(data)
    while account_a == account_b:
        account_b = random.choice(data)
#add score 