from PLayer import Player
from ComputerPlayer import ComputerPlayer
from humanPlayer import humanPlayer
    def Play(, cp, hp):
        while self.cp.stillHasShips() and self.hp.stillHasShips():
            cp.createShipGrid()
            cp.printGrids()
            hp.createShipGrid()
            hp.printGrids()
            hp.takeTurn()
            hp.printGrids()
            cp.printGrids()
            cp.takeTurn()
            hp.printGrids()
            cp.printGrids()
        if cp.stillHasShips() and not hp.stillHasShips():
            print("you lost")
        else:
            print("you win")







