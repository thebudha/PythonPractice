# Cows and Bulls Game
import random


def generate_secret():
    digits = random.sample(range(1, 10), 4)
    return ''.join(str(digit) for digit in digits)

    # secret = ''
    # #print(digits[:4])
    # for digit in digits[:4]:
    #     secret += str(digit)
    # return secret


def calculate_cows_and_bulls(secret, guess):
    # Refactored using list comprehension:
    bulls = sum([1 for i in range(4) if guess[i] == secret[i]])
    cows = sum([1 for i in range(4) if guess[i] in secret]) - bulls

    return cows, bulls

# Original logic:
    # cows = 0
    # bulls = 0

    # for i in range(4):
    #     if guess[i] == secret[i]:
    #         bulls += 1
    #     elif guess[i] in secret:
    #         cows += 1
    # return cows, bulls
    

def main():
    secret = generate_secret()
    while True:
        guess = input('Guess: ')
        if len(guess) == 4 and guess.isdigit() and len(set(guess))==4:
            cows, bulls = calculate_cows_and_bulls(secret, guess)
            print(f'{cows} cows, {bulls} bulls')

            if bulls == 4:
                print('Congratulations!  \nYou guessed the correct number.')
                break
        else:
            print('Invalid guess.')
            print('Please enter a 4 digit number with unique digits.')

            
if __name__ == '__main__':
    main()
