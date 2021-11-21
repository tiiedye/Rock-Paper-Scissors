# Rock Paper Scissors in Python
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

rps = [rock, paper, scissors]

print("Welcome to Rock, Paper, Scissors!")
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors "))
computer_choice = random.randint(0, 2)

if user_choice == 0 or user_choice == 1 or user_choice == 2:
    print("You chose:")
    print(rps[user_choice])
    print("\nComputer chose:")
    print(rps[computer_choice])

    if user_choice == computer_choice:
        print("It's a Tie!")
    elif user_choice == 0:
        if computer_choice == 1:
            print("You Lose!")
        elif computer_choice == 2:
            print("You Win!")
    elif user_choice == 1:
        if computer_choice == 0:
            print("You Win!")
        elif computer_choice == 2:
            print("You Lose!")
    elif user_choice == 2:
        if computer_choice == 0:
            print("You Lose!")
        elif computer_choice == 1:
            print("You Win!")

    print("Good Game!!")
else:
    print("Invalid choice...")
