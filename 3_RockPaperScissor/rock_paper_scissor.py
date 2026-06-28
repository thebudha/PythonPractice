import random

# NOTE:
# Call emoji picker:  Windows key + . or Windows key + ; to open on Windows. 
# On Mac, use Control + Command + Space.

ROCK = 'r'
PAPER = 'p'
SCISSORS = 's'
emojis = {ROCK: '🪨', PAPER: '📄', SCISSORS: '✂️'}
choices = tuple(emojis.keys())  # (ROCK, PAPER, SCISSORS)

def get_user_choice():
    """Prompt the user for their choice and validate it."""
    print("Welcome to Rock, Paper, Scissors!")
    while True:
        user_choice = input('Rock, paper, or scissors? (r, p, s): ').lower()
        if user_choice in choices:
            return user_choice
        else:
            print('Invalid choice! Please choose r, p, or s.')

def display_choices(user_choice, computer_choice):
    """Display the choices made by the user and the computer."""
    print(f"You chose: {emojis[user_choice]}")
    print(f"Computer chose: {emojis[computer_choice]}")

def determine_winner(user_choice, computer_choice):
    """Determine the winner based on the choices."""
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (
        (user_choice == ROCK and computer_choice == SCISSORS) or
        (user_choice == PAPER and computer_choice == ROCK) or
        (user_choice == SCISSORS and computer_choice == PAPER)):
        return "You win! 🙂"
    else:
        return "You lose! 🙁"

def play_game():
    while True:
        user_choice = get_user_choice()

        computer_choice = random.choice(choices)

        display_choices(user_choice, computer_choice)

        result = determine_winner(user_choice, computer_choice)
        print(result)

        should_continue = input("Do you want to play again? (y/n): ").lower()
        if should_continue == 'y':
            print("Let's play again!")
        else:
            print("Thanks for playing!")
            break

play_game()
        