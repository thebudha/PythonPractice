import random

# NOTE:
# Call emoji picker:  Windows key + . or Windows key + ; to open on Windows. 
# On Mac, use Control + Command + Space.

emojis = {
    "r": "🪨",  # Rock
    "p": "📃",  # Paper
    "s": "✂️"   # Scissors
}
choices = ("r", "p", "s")

def get_user_choice():
    while True:
        user_choice = input("Enter your choice (rock, paper, scissors): ").lower()
        if user_choice in choices:
            return user_choice
        else:
            print("Invalid choice! Please choose rock, paper, or scissors.")

def display_choices(user_choice, computer_choice):
    print(f'You chose {emojis[user_choice]}')
    print(f'Computer chose {emojis[computer_choice]}')

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        print("It's a tie!")
    elif(
        (user_choice == "r" and computer_choice == "s") or 
        (user_choice == "s" and computer_choice == "p") or 
        (user_choice == "p" and computer_choice == "r")):
        #print(f'Computer chose {emojis[computer_choice]}')
        print("You win!")
    else:
        #print(f'Computer chose {emojis[computer_choice]}')
        print("You lose!")

def play_game() :
    while True:
        user_choice = get_user_choice()

        computer_choice = random.choice(choices)

        display_choices(user_choice, computer_choice)

        determine_winner(user_choice, computer_choice)

        should_continue = input('Continue? (y/n): ').lower()
        if should_continue == 'n':
            break

play_game()
