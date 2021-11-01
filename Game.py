from Player import Player
from ComputerPlayer import ComputerPlayer
from SmartComputerPlayer import SmartComputerPlayer
from humanPlayer import humanPlayer
def Play(cp, hp): # this method makes each player take a turn, printing the grids after each one, untill one player has no ships left
    cp.createShipGrid()
    hp.createShipGrid()
    print(cp.stillHasShips())
    print(hp.stillHasShips())
    while cp.stillHasShips() and hp.stillHasShips():
        print("loop running again")
        cp.takeTurn(hp)
        print("cp took turn")
        hp.printGrids()
        print("printed hp grid")
        hp.takeTurn(cp)
        print("hp took turn")
        hp.printGrids()
        print("printed hp grid")
    if cp.stillHasShips() and not hp.stillHasShips():
        print("you lost")#if human player has no ships print you lost
    else:
        print("you win")#if computer player has no ships print you won


c = ComputerPlayer()
h = humanPlayer()
s = SmartComputerPlayer()
Play(s, h)







