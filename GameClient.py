from Game import Game
from ComputerPlayer import ComputerPlayer
from humanPlayer import humanPlayer
cp = ComputerPlayer()
hp = humanPlayer()
game = Game(cp, hp)
game.Play(cp, hp)