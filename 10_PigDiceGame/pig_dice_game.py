# Pig Dice Game
import random


def print_welcome_message():
    print("Welcome to the Pig Dice Game!")
    print("Rules:")
    print("- Players take turns rolling two 6-sided dice.")
    print("- On each turn, a player can roll the dice as many times as they want.")
    print("- If either die shows a 1, the player loses all points for that turn.")
    print("- If both dice show a 1, the player also loses all points for that turn.")
    print("- If a player rolls any other combination, they add the total to their turn total.")
    print("- A player can choose to hold at any time, adding their turn total to their score.")
    print("- The first player to reach 100 points wins!")
    print("Let's start the game!")


def start_game():
    while True:
        choice = input("Press Enter to begin or type 'exit'/'quit' to quit: ").strip().lower()

        if choice == "":
            print("Starting the game...")
            return

        if choice in {"exit", "quit", "q"}:
            print("Thanks for playing!")
            raise SystemExit

        print("Invalid input. Press Enter to begin or type 'exit'/'quit' to quit the game.")


def show_scoreboard(scores):
    print("\nScoreboard:")
    print(f"Player 1: {scores['Player 1']}")
    print(f"Player 2: {scores['Player 2']}")


def ask_roll_again(player_name):
    while True:
        choice = input("Roll again? (y/n): ").strip().lower()

        if choice in {"y", "yes"}:
            return True

        if choice in {"n", "no"}:
            return False

        if choice in {"quit", "exit", "q"}:
            print("Thanks for playing!")
            raise SystemExit

        print("Invalid input. Enter 'y' to roll again or 'n' to hold.")


def play_game():
    scores = {"Player 1": 0, "Player 2": 0}
    current_player = "Player 1"

    while max(scores.values()) < 100:
        turn_total = 0
        show_scoreboard(scores)
        print(f"\n{current_player}'s turn:")

        while True:
            die_1 = random.randint(1, 6)
            die_2 = random.randint(1, 6)
            roll_total = die_1 + die_2
            print(f"You rolled {die_1} and {die_2}. Total: {roll_total}.")

            if die_1 == 1 and die_2 == 1:
                print()
                print(f"******* {current_player} rolled double 1s and loses all points for this turn. *******")
                turn_total = 0
                break

            if die_1 == 1 or die_2 == 1:
                print()
                print(f"******* {current_player} rolled a 1 and loses all points for this turn. *******")
                turn_total = 0
                break

            turn_total += roll_total
            print(f"{current_player} has {turn_total} points this turn.")
            print(f"{current_player}'s total score is now {scores[current_player] + turn_total}.")
            print()

            if scores[current_player] + turn_total >= 100:
                scores[current_player] += turn_total
                print(f"{current_player} wins the game with a total score of {scores[current_player]}!")
                return

            if not ask_roll_again(current_player):
                scores[current_player] += turn_total
                print(f"{current_player} holds with a total score of {scores[current_player]}.")
                if scores[current_player] >= 100:
                    print(f"{current_player} wins the game! "
                          f"Final score: {scores[current_player]}")
                    return
                break

        current_player = "Player 2" if current_player == "Player 1" else "Player 1"


def main():
    while True:
        print_welcome_message()
        start_game()
        play_game()

        while True:
            restart_choice = input("Play again? (y/n): ").strip().lower()
            if restart_choice in {"y", "yes"}:
                print("Starting a new game...\n")
                break
            if restart_choice in {"n", "no", "quit", "exit", "q"}:
                print("Thanks for playing!")
                raise SystemExit
            print("Invalid input. Enter 'y' to play again or 'n' to quit.")


if __name__ == "__main__":
    main()
