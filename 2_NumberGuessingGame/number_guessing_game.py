import random


def play_game():
    """Run one full round of the number guessing game."""
    # Choose a random number between 1 and 100 for the player to guess.
    number_to_guess = random.randint(1, 100)
    print("Welcome to the Number Guessing Game!")

    while True:
        try:
            # Ask the player for their guess and convert it to an integer.
            guess = int(input("Guess the number between 1 and 100: "))

            # Give feedback until the player finds the correct number.
            if guess < number_to_guess:
                print("Too low!")
            elif guess > number_to_guess:
                print("Too high!")
            else:
                print("Congratulations! You guessed the number.")
                return
        except ValueError:
            # Handle non-integer input without crashing.
            print("Invalid input! Please enter a valid number.")


def main():
    """Keep playing games until the user decides to quit."""
    while True:
        play_game()
        # Ask whether the user wants to play another round.
        again = input("Play again? (y/n): ").strip().lower()
        if again not in ("y", "yes"):
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    # Only run the game loop when this script is executed directly.
    main()
