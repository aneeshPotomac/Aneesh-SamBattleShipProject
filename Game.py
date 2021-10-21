from ComputerPlayer import ComputerPlayer
from humanPlayer import humanPlayer
class Game:
    def __init__(self, cp, hp):
        pass

    def Play(self, cp, hp):
        while cp.stillHasShips() and hp.stillHasShips():
            cp.createShipGrid()
            hp.createShipGrid()







