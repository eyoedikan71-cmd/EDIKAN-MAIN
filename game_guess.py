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

# args = parser.parse_args()
# parser = argparse.ArgumentParser(description="Choose a level of the game")
parser.add_argument("--difficulty",type=str,choices=["easy", "medium", "hard"],
        required=True,
        help="Choose difficulty level: easy, medium, hard")
parser.add_argument(
    "--guesses",
    nargs="+",
    type=int,
    required=True,
    help="List of guesses the user inputs"
)
args = parser.parse_args()

levels = {
    "easy": 10,
    "medium": 7,
    "hard": 5
}
attempts = levels.get(args.difficulty)
number = random.randint(1, 100)
attempt_count = 0
print(f"Hello {args.name}! Welcome to the Number Guessing Game! \nI'm thinking of a number between 1 and 100.")
print(f"Difficulty: {args.difficulty} which is what you chosed")  


print("\nLet's begin the game!")
for guess in args.guesses:
    if attempt_count >= attempts:
        break

    attempt_count += 1
    print(f"Attempt {attempt_count}/{attempts}: You guessed {guess}")

    if guess == number:
        print(f"\nCongratulations! The number was {number}.")
        print(f"You won in {attempt_count} attempts.")
        break

    elif guess > number:
        print("Too high")
    else:
        print("Too low")

if attempt_count >= attempts and guess != number:
    print(f"\nOut of attempts! The number was {number}.")


