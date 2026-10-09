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


#generate a random account from the data
account_a = random.choice(data)
account_b = random.choice(data)
if account_a== account_b:
    account_b = random.choice(data)

#format account data into printable format 
print(f"Compare A: {format_data(account_a)}. ")
print(f"Compare B: {format_data(account_b)}. ")
#ask user for guess

guess = input("who has more followers? Type 'A' or 'B: ").lower()
#check if user is correct
# - get follower count of each accoiunt
# use if statement to chck if user is correct

#give user feedback on their guess

#score keeping

#make the game repeatable 

#making account at posigion b becomes the next account at position A


