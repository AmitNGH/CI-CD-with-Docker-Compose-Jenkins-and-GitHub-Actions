import MainScores
import Live
import multiprocessing
from time import sleep


score_main_thread = multiprocessing.Process(target=MainScores.run_score_main)
score_main_thread.start()

sleep(1)

print(Live.welcome("Amit"))
Live.load_game()

score_main_thread.terminate()
