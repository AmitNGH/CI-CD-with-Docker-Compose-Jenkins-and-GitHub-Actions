from requests import get
from Util import get_user_input_and_validate
from random import randint

api_url = "https://v6.exchangerate-api.com/v6/45f3830387d754dcb21676b3/latest/USD"


def get_money_interval(difficulty, generated_num):

    exchange_rate = get(api_url).json()['conversion_rates']['ILS']

    total_value = exchange_rate * generated_num
    return total_value + (5 - difficulty), total_value - (5 - difficulty)


def get_guess_from_user():
    return get_user_input_and_validate(f"Enter your guess of the current exchange rate betweeמ USD to ILS ",
                                       "Guess should be a number, please try again - ",
                                       "",
                                       float)


def play(difficulty):
    print("Welcome to Currency Roulette!")
    generated_num = randint(1, 100)

    print(f"The number is {generated_num} USD, what is the value of the number in ILS?")
    user_guess = get_guess_from_user()

    interval = get_money_interval(difficulty, generated_num)

    if interval[0] <= user_guess <= interval[1]:
        print("Congratulations! You Won")
        return True
    else:
        print(f"Sorry, You did not guess correct, Better luck next time.")
        return False
