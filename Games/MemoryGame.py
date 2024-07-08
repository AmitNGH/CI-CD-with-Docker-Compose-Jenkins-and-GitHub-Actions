from random import randint
from time import sleep
from Utils.Utils import get_user_input_and_validate


def generate_sequence(difficulty):
    generated_numbers = []
    for i in range(difficulty):
        generated_numbers.append(randint(1, 101))

    return generated_numbers


def get_guess_from_user(difficulty):

    print(f"Enter the {difficulty} numbers you remember, Press the Enter key between each number")

    user_guess = []
    for i in range(difficulty):
        user_guess.append(get_user_input_and_validate("",
                                                      "Guess should be a number, please try again - ",
                                                      "Guess not in range, please try again - ",
                                                      int,
                                                      range(1, 102)))

    return user_guess


def is_list_equal(first_list, second_list):
    first_list.sort()
    second_list.sort()

    return first_list == second_list


def play(difficulty):
    print("Welcome to memory game - remember those numbers!")
    sleep(2)

    generated_numbers = generate_sequence(difficulty)
    print(generated_numbers, end="")
    sleep(0.7)
    print("\r", end="")

    user_guess = get_guess_from_user(difficulty)

    if is_list_equal(generated_numbers, user_guess):
        print("Congratulations! You guessed the right numbers")
        return True
    else:
        print(f"Sorry, The numbers are {generated_numbers}")
        return False
