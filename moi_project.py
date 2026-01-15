import argparse
import random
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
parser = argparse.ArgumentParser(description="A Rock, Paper and scissors game.")
parser.add_argument("name",type=str,help="Your name")
args = parser.parse_args()

g_options = ['rock', 'paper','scissors']
while True:
    user_input = input(f"Welcome {args.name} to the 'Rock Paper Scissors' game\nChoose between rock, paper and scissors(or type 'quit' to exit): "
    ).lower()

    # exit condition
    if user_input == 'quit':
        logging.info("Exiting from the game... Goodbye!")
        break

    if user_input not in g_options:
        logging.info("Invalid option. Please select rock, paper, or scissors.")
        continue
    comp_option = random.choice(g_options)
    logging.info(f"You choose '{user_input}' and the computer chooses '{comp_option}'")


    if user_input == comp_option:
        logging.info(f"Your guess - '{user_input}' and comp's guess - '{comp_option}' are the same!\n You can try again, u might win!")
    elif user_input == 'rock':
        if comp_option == 'paper':
            logging.info("You lose because PAPER covers ROCK\nPlease try again!")
        else:
            logging.info("Congratulations!, you win because ROCK smashes SCISSORS.")
                
    elif user_input == 'paper':
        if comp_option == 'scissors':
            logging.info("You lose because SCISSORS cuts PAPER\nPlease try again!")
        else:
            logging.info("Congratulations!, you win because PAPER covers ROCK.")

    elif user_input == 'scissors':
        if comp_option == 'rock':
            logging.info("You lose because ROCK smashes SCISSORS\nPlease try again!")
        else:
            logging.info("Congratulations!, you win because SCISSORS cuts PAPER.")

    if user_input not in g_options:
        logging.info("Please try again and select a valid option")
        


       
    # # if user_input == 'quit':
    #     # continue            1
    # break 
    # if user_input == 'quit':
    #     continue
    # else:
    #     break    

# reponses = {"hi": ["Hey!", "Yoo! how are you doing today?"], "hello": ["Hi there" , "Whats up!"] "hey": ["Hello", "hi!"],
#     "bye": ["Bye!, see ya"],
#     "how are you": ["I'm doing great!, and you?"], "what do you do": ["I'm just a simple chat bot, fun to interact with."]
#     "how can you help me": ["One way is by eliminating boredom. You are free the interact with me anytime you wish."]
#     "are you a human?": ["Sorry!, no i'm not a human but just a simple Chatbot."]
#     "can you do something for me?": ["Perhaps, maybe i can.\n What's the matter let me see if i can find a solution."]}

# print("Welcome, this is Chatbot...feel free to interact")

