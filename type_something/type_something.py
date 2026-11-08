from type_something_art import logo
import random

EASY_LEVEL_TURNS = 6
HARD_LEVEL_TURNS = 5
attempts = 0
guess = 0

# Choosing easy level - a random number between 1 and 100
random_number_easy = random.randint(1, 100)

# Choosing hard level - a random number between 500 and 1000 -
random_number_hard = random.randint(500, 1000)

def rand_num(difficulty_level):
    return random_number_easy if difficulty_level == 'easy' else random_number_hard
def turns(difficulty_level):
    return EASY_LEVEL_TURNS if difficulty_level == 'easy' else HARD_LEVEL_TURNS

def difficulty_level_easy(difficulty_level):
    """Function to set difficulty"""
    print("I am thinking of a number between 1 and 100")
    print(f"You have given {EASY_LEVEL_TURNS} attempts to guess the number.")

def difficulty_level_hard(difficulty_level):
    print("I am thinking of a number between 500 and 1000")
    print(f"You have given {HARD_LEVEL_TURNS} attempts to guess the number.")

def check_answer(user_guess, actual_answer, turns_left):
    """
    Function to check User's guess against actual answer
    Track the number of turns and reduce by 1 if they get it wrong"""
    global attempts
    global guess
    if guess == actual_answer:
        print(f"You got it! The answer is {guess}")
    elif guess > actual_answer:
        turns_left -= 1
        print("Too high!")
    elif guess < actual_answer:
        turns_left -= 1
        print("Too low!")
    attempts = turns_left

def attempts_left():
    print(f"{attempts} attempts remaining to guess the number.")

def user_choice():
    print("Welcome to the Number Guessing Game!")
    while True:
        difficulty_level = input("Choose a difficulty level - Type 'easy' or 'hard': hard: ")
        if difficulty_level not in ['easy', 'hard']:
            print("Please enter a valid input")
            continue
        return difficulty_level

def game():
    global attempts
    global guess
    should_continue = True
    print(logo)

    difficulty_level = user_choice()
    if difficulty_level == "easy":
        difficulty_level_easy(difficulty_level)
    elif difficulty_level == "hard":
        difficulty_level_hard(difficulty_level)
    answer = rand_num(difficulty_level)
    attempts = turns(difficulty_level)

    while should_continue:
        '''Repeat the guessing functionality if they get it wrong'''
        try:
            # Let the user guess a number
            guess = int(input("Make a guess: "))

            check_answer(guess, answer, attempts)
            if guess == answer:
                should_continue = False
            elif attempts == 0:
                print("You ran out of attempts! You lose!")
                should_continue = False
            else:
                attempts_left()
        except ValueError:
            print("Please type a valid input")
game()
