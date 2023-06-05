from game import Game
from exception import GameOverException, GameOverCroupierException, GameOverUserException

try:
    game = Game()
    game.play()
    game.have_fun()
except GameOverCroupierException:
    print('Wygrywa gracz!')
except GameOverUserException:
    print('Wygrywa krupier!')