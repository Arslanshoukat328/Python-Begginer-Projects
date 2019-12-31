31-DEC-2019

import random


hand = ("rock", "paper", "scissors")
tri_no = int(0)
tri_limit = int(3)
user_points = int(0)
computer_points = int(0)

while tri_no < tri_limit:
    user_choice = (input("try.   ")).lower()
    computer_choice = random.choice(hand)
    tri_no += 1
    if user_choice == computer_choice:
        print("You both choose the same answer")
    elif user_choice == "rock":
        if computer_choice == "paper":
            print("You lost")
            computer_points += 1
        elif computer_choice == "scissors":
            print("You Won.")
            user_points += 1
    elif user_choice == "paper":
        if computer_choice == "rock":
            print("You won.")
            user_points += 1
        elif computer_choice == "scissors":
            print("you lost")
            computer_points += 1
    elif user_choice == "scissors":
        if computer_choice == "rock":
            print("You won")
            user_points += 1
        elif computer_choice == "paper":
            print("You lost")
            computer_points += 1

print(f'The user won {user_points} round(s).')
print(f'The computer won {computer_points} round(s) ')
