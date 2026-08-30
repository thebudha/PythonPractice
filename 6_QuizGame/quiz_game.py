import random
from termcolor import cprint

QUESTION = "questions"
OPTIONS = "options"
ANSWER = "answer"



def ask_question(index, question, options):
    print(f"Question {index}: {question}")
    for option in options:
        print(option)
    
    return input("Your answer: ").strip().upper()

def run_quiz(quiz):
    random.shuffle(quiz)

    score = 0

    for index, item in enumerate(quiz, 1):
        answer = ask_question(index, item[QUESTION], item[OPTIONS])
        
        if answer == item[ANSWER]:
            cprint("Correct!", "green")
            score += 1
        else:
            cprint(f"Wrong! The correct answer is {item[ANSWER]}", "red")

        print()

    cprint(f"Quiz over! Your final score is {score} out of {len(quiz)}", "blue")

def main():
    quiz = [
        {
            QUESTION: "What is the capital of France?",
            OPTIONS: ["A. Berlin", "B. Madrid", "C. Paris", "D. Rome"],
            ANSWER: "C"
        },
        {
            QUESTION: "What planet is known as the Red Planet?",
            OPTIONS: ["A. Earth", "B. Mars", "C. Jupiter", "D. Saturn"],
            ANSWER: "B"
        },
        {
            QUESTION: "What is the largest ocean on Earth?",
            OPTIONS: ["A. Atlantic", "B. Indian", "C. Arctic", "D. Pacific"],
            ANSWER: "D"
        },
        {
            QUESTION: "Which vertibrates live both in water and on land?",
            OPTIONS: ["A. Reptiles", "B. Amphibians", "C. Birds", "D. Mammals"],
            ANSWER: "B"
        },
        {
            QUESTION: "What is the largest internal organ in the human body?",
            OPTIONS: ["A. Liver", "B. Heart", "C. Lungs", "D. Kidneys"],
            ANSWER: "A"
        },
        {
            QUESTION: "Which country is the band, AC/DC from?",
            OPTIONS: ["A. United States", "B. United Kingdom", "C. Australia", "D. Canada"],
            ANSWER: "C"
        },
        {
            QUESTION: "What is the atomic number of hydrogen?",
            OPTIONS: ["A. 1", "B. 2", "C. 3", "D. 4"],
            ANSWER: "A"
        },
        {
            QUESTION: "Which member of the Spice Girls was known as 'Sporty Spice'?",
            OPTIONS: ["A. Victoria Beckham", "B. Melanie Brown", "C. Melanie Chisholm", "D. Emma Bunton"],
            ANSWER: "C"
        },
        {
            QUESTION: "What is the largest planet in our solar system?",
            OPTIONS: ["A. Jupiter", "B. Saturn", "C. Uranus", "D. Neptune"],
            ANSWER: "A"
        },
        {
            QUESTION: "Which of the following is not a fruit?",
            OPTIONS: ["A. Avocado", "B. Tomato", "C. Rhubarb", "D. Orange"],
            ANSWER: "C"
        }
    ]
    run_quiz(quiz)

if __name__ == "__main__":
    main()