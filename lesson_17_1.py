#Game “Rock, Paper, Scissors, Lizard, Spock”

import random


choices = {
    'rock': ["scissors", "lizard"],
    'paper': ["rock", "spock"],
    'scissors': ["paper", "lizard"],
    'lizard': ["spock ", "paper"],
    'spock': ["scissors", "rock"],
}

# if computer in choices[user]:
#     print('user win')

while True:

    user = input("Your choice (rock, paper, scissors, lizard, spock)?: ")
    possible_actions = ["rock", "paper", "scissors", "lizard", "spock"]
    computer = random.choice(possible_actions)

    if user.lower() in possible_actions:
        print(f"\nPlayer: {user} \nComputer: {computer}\n")
    elif user.lower() not in possible_actions:
        print("Invalid input", user)

    if user == computer:
        print("It's a TIE!")
    elif computer in choices[user]:
        print('Player WIN!')
    else:
        print('Computer WIN')
    #
    # elif user == "rock":
    #     # if computer == "scissors" or computer == "lizard":
    #     if computer in ["scissors", "lizard"]:
    #         print("Player WIN!")
    #     else:
    #         print("Player LOSE!.")
    # elif user == "paper":
    #     if computer == "rock" or computer == "spock":
    #         print("Player WIN!")
    #     else:
    #         print("Player LOSE!.")
    # elif user == "scissors":
    #     if computer == "paper" or computer == "lizard":
    #         print("Player WIN!")
    #     else:
    #         print("Player LOSE!.")
    # elif user == "lizard":
    #     if computer == "spock " or computer == "paper":
    #         print("Player WIN!")
    #     else:
    #         print("Player LOSE!.")
    # elif user == "spock":
    #     if computer == "scissors" or computer == "rock":
    #         print("Player WIN!")
    #     else:
    #         print("Player LOSE!.")

    play_again = input("Play again? (y/n): ")

    if play_again.lower() == "y":
        continue
    if play_again.lower() == "n":
        break
    elif play_again.lower() != 'y' or 'n':
        print("Invalid input:", play_again)