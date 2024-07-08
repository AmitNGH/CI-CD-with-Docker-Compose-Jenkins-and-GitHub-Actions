from Games.Games import get_games
from Utils.ConfigHandler import read_config
from Utils.Utils import get_user_input_and_validate


def welcome(name):
    return (f"Hello {name} and welcome to the World of Games (WoG).\n"
            "Here you can find many cool games to play.")


def load_game():
    config_values = read_config()

    max_difficulty = config_values.get('max_difficulty')
    is_valid_difficulty = False

    chosen_game = get_user_input_and_validate("Please choose a game to play: \n"
                                              "1. Memory Game - a sequence of numbers will appear for 1 second and "
                                              "you have to guess it"
                                              "back\n"
                                              "2. Guess Game - guess a number and see if you chose like the computer\n"
                                              "3. Currency Roulette - try and guess the value of a random amount of "
                                              "USD in ILS\n",
                                              "Game input should be a number, please try again - ",
                                              "Game not found, please try again - ",
                                              int,
                                              range(1, len(Games.get_games()) + 1))

    difficulty = get_user_input_and_validate(f"Please choose game difficulty from 1 to {max_difficulty}: ",
                                             "Difficulty should be a number, please try again - ",
                                             "Invalid difficulty, please try again - ",
                                             int,
                                             range(1, max_difficulty + 1))

    get_games().get(chosen_game)(difficulty)
