import Live as Live
import Utils.Utils as Utils
from time import sleep

sleep(1)

print(Live.welcome("Amit"))

playing = True

while playing:
    Live.load_game()
    continue_playing = difficulty = Utils.get_user_input_and_validate(f"Do you want to play another game? enter y/n ",
                                                                      "Invalid input, please enter y/n",
                                                                      "Invalid input, please enter y/n",
                                                                      str,
                                                                      ["y", "n"])

    if continue_playing == "n":
        playing = False
