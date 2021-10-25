from Player import Player
from ComputerPlayer import ComputerPlayer
from humanPlayer import humanPlayer
def Play(cp, hp):
    cp.createShipGrid()
    hp.createShipGrid()
    while cp.stillHasShips() and hp.stillHasShips():
        cp.printGrids()
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

c = ComputerPlayer()
h = humanPlayer()
Play(c,h)







