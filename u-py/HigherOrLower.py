import random
from Game_data import data
from replit import clear

clear()

def get_data():
    return random.choice(data)




def display_data(account):
    name = account["name"]
    des = account["description"]
    country = account["country"]
    print(f"{name}, a {des}, from {country}")


def compare_accounts(account_a,account_b):
    if account_a["follower_count"] > account_b["follower_count"]:
        return account_a
    else:
        return account_b





account_a=get_data()
account_b=get_data()
display_data(account_a)
display_data(account_b)
a=compare_accounts(account_a,account_b)
print(display_data(a))