import random


def play_game():
    number_to_guess = random.randint(1, 100)
    print("Welcome to the Number Guessing Game!")

    while True:
        try:
            guess = int(input("Guess the number between 1 and 100: "))

            if guess < number_to_guess:
                print("Too low!")
            elif guess > number_to_guess:
                print("Too high!")
            else:
                print("Congratulations! You guessed the number.")
                return
        except ValueError:
            print("Invalid input! Please enter a valid number.")


def main():
    while True:
        play_game()
        again = input("Play again? (y/n): ").strip().lower()
        if again not in ("y", "yes"):
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    main()
