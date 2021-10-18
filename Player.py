from Grid import Grid

class Player:

    def __init__(self):
        self.gridShips = Grid()
        self.gridShots = Grid()

    def takeTurn(self, otherPlayer ):
        # over write in the HumanPlayer and ComputerPlayer subclasses
        pass

    def placeShip(self, ship , size ):
        # over write in the HumanPlayer and ComputerPlayer subclasses
        pass

    def stillHasShips(self):
        # over write in the HumanPlayer and CounterPlayer subclasses
        pass

    # This is a useful method to determine if the space is "~" or something else
    # Send it the grid you want to check, so ship or shot
    def createShipGrid(self):
        placeShip( "A" , 5 )
        placeShip( "B", 4 )
        placeShip( "C", 3 )
        placeShip( "S", 3 )
        placeShip( "D", 2 )

    def printGrids(self):
        print("Ship Grid")
        self.gridShips.printGrid()
        print("Shot Grid")
        self.gridShots.printGrid()
