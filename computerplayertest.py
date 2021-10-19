from ComputerPlayer import ComputerPlayer

comp_player = ComputerPlayer()
comp_player.createShipGrid()
print("printing first grid: comp_player")
comp_player.printGrids()
opp = ComputerPlayer()
opp.createShipGrid()
print("printing second grid: opp")
opp.printGrids()
comp_player.takeTurn(opp)
print("printing third grid: comp_player")
comp_player.printGrids()
print("printing fourth grid: opp")
opp.printGrids()

