import MainScores
from Live import load_game, welcome
from threading import Thread
from time import sleep

score_main_thread = Thread(target=MainScores.run_score_main)
score_main_thread.start()

sleep(1)

print(welcome("Amit"))
load_game()
