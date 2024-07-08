from Utils.Utils import read_file
from Utils.Utils import write_to_file
from Utils.Utils import SCORES_FILE_NAME


def add_score(difficulty):
    current_score = 0
    points_of_winning = (difficulty * 3) + 5

    try:
        current_score = read_file(SCORES_FILE_NAME)
    except IOError:
        pass
    finally:
        write_to_file(SCORES_FILE_NAME, current_score + points_of_winning)

