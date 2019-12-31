import random

golden_number = random.randint(0, 20)
guess_no = 0
guess_limit = 3

if guess_no < guess_limit:
    guess = int(input("Guess any number in between 0 - 20.   "))
    guess_no += 1
    if guess == golden_number:
        print('Congratulation, You made the right choice.')
    elif guess < golden_number:
        print('Your guess is too high.')
    elif guess > golden_number:
        print('Your guess is to low')
