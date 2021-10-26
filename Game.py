from Player import Player
from ComputerPlayer import ComputerPlayer
from humanPlayer import humanPlayer
def Play(cp, hp):
    cp.createShipGrid()
    hp.createShipGrid()
    print(cp.stillHasShips())
    print(hp.stillHasShips())
    while cp.stillHasShips() and hp.stillHasShips():
        print("loop running again")
        cp.printGrids()
        print("printed cp grids")
        cp.takeTurn(hp)
        print("cp took turn")
        cp.printGrids()
        print("printed cp grid")
        hp.printGrids()
        print("printed hp grid")
        hp.takeTurn(cp)
        print("hp took turn")
        hp.printGrids()
        print("printed hp grid")
        cp.printGrids()
        print("printed cp grid")
    if cp.stillHasShips() and not hp.stillHasShips():
        print("you lost")
    else:
        print("you win")


c = ComputerPlayer()
h = humanPlayer()
Play(c, h)







