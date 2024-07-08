from random import randint
from Utils import get_user_input_and_validate


def generate_number(difficulty):
    return randint(1, difficulty)


def get_guess_from_user(difficulty):
    return get_user_input_and_validate(f"Please enter a number between 1 to {difficulty} - ",
                                       "Guess should be a number, please try again - ",
                                       "Guess not in range, please try again - ",
                                       int,
                                       range(1, difficulty + 1))


def compare_results(secret_number, user_guess):
    return secret_number == user_guess


def play(difficulty):
    print("Welcome to Guess Game! - guess the secret number")

    secret_number = generate_number(difficulty + 1)
    user_guess = get_guess_from_user(difficulty + 1)

    if compare_results(secret_number, user_guess):
        print("Congratulations! You guessed the right number")
        return True
    else:
        print(f"Sorry, The secret number was {secret_number}")
        return False
