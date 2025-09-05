# Rock, Paper, Scissors Game
# A simple command-line implementation of the classic game.
# The player chooses Rock, Paper, or Scissors, and the computer responds with a random choice.
# The winner is determined by standard game rules.

# Importing random module

import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Images stored in a list for easy access by index
game_images = [rock, paper, scissors]

# User is prompted to select one option from 0 (Rock), 1 (Paper), or 2 (Scissors)
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if user_choice >= 0 and user_choice <= 2:
    print(game_images[user_choice])

# Computer randomly selects 0 (Rock), 1 (Paper), or 2 (Scissors)
computer_choice = random.randint(0,2)
print("Computer chose: ")
print(game_images[computer_choice])

# Conditions for game result using logical operators
if user_choice >= 3 or user_choice < 0:
    print("You selected incorrect value. You lose.")
elif user_choice == 0 and computer_choice == 2:
     print("You win!")
elif computer_choice == 0 and user_choice == 2:
    print("You lose!")
elif user_choice > computer_choice:
    print("You win!")
elif computer_choice > user_choice:
    print("You lose!")
elif computer_choice == user_choice:
    print("It's a draw!")
