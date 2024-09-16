from .GuessGame import play as playGuessGame
from .MemoryGame import play as playMemoryGame
from .CurrencyRouletteGame import play as playCurrencyRouletteGame


def get_games():
    return {1: playMemoryGame,
            2: playGuessGame,
            3: playCurrencyRouletteGame}
