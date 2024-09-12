from Score import add_score
import Games.Games as Games
import Utils.ConfigHandler as ConfigManager
import Utils.Utils as Utils


def welcome(name):
    return (f"Hello {name} and welcome to the World of Games (WoG).\n"
            "Here you can find many cool games to play.")


def load_game():
    config_values = ConfigManager.read_config()

    max_difficulty = config_values.get('max_difficulty')

    chosen_game = Utils.get_user_input_and_validate("Please choose a game to play: \n"
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

    difficulty = Utils.get_user_input_and_validate(f"Please choose game difficulty from 1 to {max_difficulty}: ",
                                                   "Difficulty should be a number, please try again - ",
                                                   "Invalid difficulty, please try again - ",
                                                   int,
                                                   range(1, max_difficulty + 1))

    if Games.get_games().get(chosen_game)(difficulty):
        add_score(difficulty)
