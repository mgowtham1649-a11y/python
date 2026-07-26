import random
game_list=["rock", "paper", "scissors"]
user_choice=int(input("enter your choice?:type 0 it rock,type 1 it paper, type 2 it scissors:"))
if user_choice < 0 or user_choice > 2:
    print("invalid choice")
else:
    print(game_list[user_choice])
    computer_choice=random.randint(0,2)
    print("computer choice:",game_list[computer_choice])
    if user_choice == computer_choice:
        print("tie")
    elif user_choice == 0 or computer_choice == 2:
        print("you win")
    elif user_choice == 2 or computer_choice == 0:
        print("you lose")
    elif user_choice > computer_choice:
        print("you win")
    else:
        print("you lose")
