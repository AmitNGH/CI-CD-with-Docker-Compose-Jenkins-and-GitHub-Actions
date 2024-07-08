import configparser


def read_config():
    config = configparser.ConfigParser()
    config.read('config.ini')

    max_difficulty = config.getint('General', 'max_difficulty')

    return {'max_difficulty': max_difficulty}