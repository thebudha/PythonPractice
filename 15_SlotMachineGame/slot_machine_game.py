import random

def get_starting_balance():
    while True:
        try:
            balance = int(input("Enter your starting balance: $"))
            if balance <= 0:
                print("Balance must be a positive number.")
            else:
                return balance
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def get_bet_amount(balance):
    while True:
        try:
            bet = int(input("Enter your bet amount: $"))
            if bet <= 0:
                print("Bet must be a positive number.")
            elif bet > balance:
                print("Bet cannot exceed your current balance.")
            else:
                return bet
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def spin_reels():
    symbols = ['🍒', '🍋', '🔔', '⭐', '🍉']
    return [random.choice(symbols) for _ in range(3)]


def display_reels(reels):
    print(f'{reels[0]} | {reels[1]} | {reels[2]}')


def calculate_payout(reels, bet):
    if reels[0] == reels[1] == reels[2]:
        return bet * 10  # Jackpot
    if reels[0] == reels[1] or reels[0] == reels[2] or reels[1] == reels[2]:
        return bet * 2  # Two of a kind
    return 0  # No win


def main():
    balance = get_starting_balance()

    print("Welcome to the Slot Machine Game!")
    print(f"Your starting balance is: ${balance}.\n")

    while balance > 0:
        print(f"Current balance: ${balance}")
        
        bet = get_bet_amount(balance)
        reels = spin_reels()
        display_reels(reels)
        payout = calculate_payout(reels, bet)
   
        if payout > 0:
            print(f"Congratulations! You won ${payout}!")
        else:
            print("You lost!")

        balance += payout - bet
        if balance <= 0:
            print("You have run out of money. Game over!")
            break

        while True:
            play_again = input('Do you want to play again? (y/n): ').strip().lower()
            if play_again in ('y', 'n'):
                break
            print("Invalid input. Please enter 'y' or 'n'.")

        if play_again == 'n':
            print(f"You are walking away with ${balance}.")
            break


if __name__ == "__main__":
    main()