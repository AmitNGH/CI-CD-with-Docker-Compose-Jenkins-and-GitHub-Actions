from Utils import read_file
from Utils import write_to_file
from Utils import SCORES_FILE_NAME


def add_score(difficulty):
    points_of_winning = (difficulty * 3) + 5
    current_score = get_score()
    write_to_file(SCORES_FILE_NAME, current_score + points_of_winning)


def get_score():
    try:
        return int(read_file(SCORES_FILE_NAME))
    except (IOError, ValueError):
        return 0
