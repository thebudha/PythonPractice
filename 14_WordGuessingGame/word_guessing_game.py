import random
import re

def read_words():
    try:
        with open("words.txt", "r") as file:
            words = file.read().splitlines()
        return words
    except FileNotFoundError:
        print("Error: File does not exist.")
        return []


def display_word(secret_word, guessed_letters):
    word_to_display = ""
    for letter in secret_word:
        if letter in guessed_letters:
            word_to_display += letter
        else:
            word_to_display += "_"

    print(word_to_display)


def get_user_guess(guessed_letters):
    while True:
        guess = input("Guess a letter: ").lower()
        if len(guess) != 1:
            print('Enter only one letter.')
        elif re.fullmatch('[a-z]', guess) is None:
            print ('Enter only letters from a-z.')
        elif guess in guessed_letters:
            print('You have already guessed that letter.')
        else:
            return guess


def is_word_guessed(secret_word, guessed_letters):
    for letter in secret_word:
        if letter not in guessed_letters:
            return False
    return True


def main():
    words = read_words()
    if not words:
        print("No words available to play the game.")
        return
    secret_word = random.choice(words)
    print(secret_word)  

    attempts = 6
    guessed_letters = []
    while attempts > 0:
        display_word(secret_word, guessed_letters)

        guess = get_user_guess(guessed_letters)
        guessed_letters.append(guess)
        attempts -= 1

        if guess in secret_word:
            print ("Good guess!")
            if is_word_guessed(secret_word, guessed_letters):
                print("Congratulations! You've guessed the word:")
                break
        else:
            print ("Wrong guess!")
        if attempts == 0:
            print("Sorry, you've run out of attempts. The word was:", secret_word)
        

if __name__ == "__main__":
    main()