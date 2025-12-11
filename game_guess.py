# import argparse
# parser = argparse.ArgumentParser(description="A number guessing game.")
# parser.add_argument("name", type=str, default="students", help="Your name")

# args = parser.parse_args()

# name = args.name
# print(name)


# what can i use to ramomly select a number

# i want to use argparse so the user can write in his terminal instead of me using input, 
# to print what the code says or what he wants to see(code).Then i will now write what i 
# want the user to see after the user has written his name in his terminal.
# The computer should randomly select a number between 1 and 100.The user shoul now choose a level which will
# determine how many chances he has to guess the correct number and

import argparse
import random

parser = argparse.ArgumentParser(description="A number guessing game.")
parser.add_argument("name",type=str,help="Your name")

args = parser.parse_args()
parser = argparse.ArgumentParser(description="Choose a level of the game")
parser.add_argument("--difficulty",type=str,choices=["easy", "medium", "hard"],
        required=True,
        help="Choose difficulty level: easy, medium, hard")
print(f"Hello {args.name}! Welcome to the Number Guessing Game! \nI'm thinking of a number between 1 and 100.You have 5 chances to guess the correct number.\nPlease select the difficulty level:\n1. Easy (10 chances)\n2. Medium (5 chances)\n3. Hard (3 chances).")
choice = print(input("\nEnter your choice of level: "))
while choice not in ["easy", "medium", "hard"]:
    print("Invalid choice. Please choose 'easy', 'medium', or 'hard'.")
    choice = input("Enter your choice of level: ")
    print(choice)
    continue

if args == "easy":
    attempts = 10
elif args == "medium":
    attempts = 5
# elif args == "hard":
#     attempts = 3    
else:  # hard
    attempts = 3
print(choice)
print("\nLet's begin the game!")
continue_game = True 
while continue_game and attempts > 0:
   print(f"You have {attempts} attempts remaining to guess the number.")
   
   break

parser = argparse.ArgumentParser(description="Choose a number")
parser.add_argument("number",type=int,help="Your chosen number")
args = random.randint(1, 100)
user_choice = input("Your number: ")
if args == user_choice:
    print(f"You picked a number btw 1 and 100: {args} but u have to choose the level first.")
else:
    print("Wrong guess,try again!")

# choice = print(input("\nEnter your choice of level: "))
# print(choice)

# import random
# args = random.randint(1, 100)
# print(args)
# # secret = random.randint(1, args)

# print(f"I picked a number between 1 and {args}")
