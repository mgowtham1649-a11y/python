import random
import os

# Logo
logo = """
 _   _ _       _               
| | | (_)     | |              
| |_| |_  __ _| |__   ___ _ __ 
|  _  | |/ _` | '_ \ / _ \ '__|
| | | | | (_| | | | |  __/ |   
\_| |_/_|\__, |_| |_|\___|_|   
          __/ |                
         |___/    LOWER GAME
"""

vs = """
 _    __
| |  / /
| | / / 
| |/ /  
|   <   
| |\ \  
|_| \_\ 
"""

# Data
data = [
    {"name": "Instagram", "followers": 600, "description": "Social Media"},
    {"name": "Cristiano Ronaldo", "followers": 550, "description": "Footballer"},
    {"name": "Lionel Messi", "followers": 500, "description": "Footballer"},
    {"name": "Selena Gomez", "followers": 430, "description": "Singer"},
    {"name": "Kylie Jenner", "followers": 400, "description": "Celebrity"},
    {"name": "Dwayne Johnson", "followers": 380, "description": "Actor"},
]

def get_random_account():
    return random.choice(data)

def format_data(account):
    name = account["name"]
    desc = account["description"]
    return f"{name}, a {desc}"

def check_answer(user_guess, a_followers, b_followers):
    if a_followers > b_followers:
        return user_guess == "a"
    else:
        return user_guess == "b"

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


# Game start
score = 0
game_should_continue = True

account_a = get_random_account()
account_b = get_random_account()

while game_should_continue:
    clear()
    print(logo)
    print(f"Score: {score}")

    # next round setup
    account_a = account_b
    account_b = get_random_account()

    # same account avoid
    while account_a == account_b:
        account_b = get_random_account()

    print(f"Compare A: {format_data(account_a)}")
    print(vs)
    print(f"Against B: {format_data(account_b)}")

    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    a_followers = account_a["followers"]
    b_followers = account_b["followers"]

    is_correct = check_answer(guess, a_followers, b_followers)

    if is_correct:
        score += 1
        print("Correct!")
    else:
        game_should_continue = False
        print(f" Wrong! Final score: {score}")