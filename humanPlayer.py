from Player import Player

class humanPlayer(Player) :
    def __init__(self):
        super().__init__()

    def placeShip(self, ship, size):
        selectionIsValid = False
        while selectionIsValid == False : #asks the user to input a coordinate point and a direction and then checks to see if there a valid spaces from that point in that direction
            locationRow = int(input("what row do you want your ship in?"))
            locationCol = int(input("what column do you want your ship in?"))
            direction = str(input("what direction do you want to place the ship"))
            selectionIsValid = True
            if locationRow + size > 10 or locationCol + size > 10 : #if the location plus the size is under 10 and thus inside the grid
                selectionIsValid = False
                continue
            if direction == "down" : #if the user selects down
                for i in range(size)  : #checks each space in column that a ship piece would be placed to see if it is valid, if any are not set selectionIsValid to false
                    if not self.gridShips.isSpaceWater(locationRow + i, locationCol) :
                        selectionIsValid = False
            if direction == "right" : #if the user selects right
                for i in range(size) :
                    if not self.gridShips.isSpaceWater(locationRow, locationCol + i) : #checks each space in the row that a ship piece would be placed to see if it is valid, if any are not set selectionIsValid to false
                        selectionIsValid = False
            if selectionIsValid == False :
                continue
            else : #if all the code has been run and selectionIsValid is true than change the selected coordinate points to the ship value
                if direction == "down" :
                    self.gridShips.changeCol(locationCol , ship , locationRow , size)
                    self.printGrids()
                if direction == "right" :
                    self.gridShips.changeRow(locationRow, ship, locationCol, size)
                    self.printGrids()

    def takeTurn(self, otherPlayer):
        shotSelection = False
        while shotSelection == False : #asks the user for a point to shoot
            shotLocationRow = int(input("what row"))
            shotLocationCol = int(input("what column"))
            if shotLocationRow <= 9 and shotLocationCol <= 9 : #if the point is within the 10x10 gird
                if not otherPlayer.gridShips.isSpaceWater(shotLocationRow,shotLocationCol) : #if the space is a ship print hit and update both the gridShot of the player and the gidShips of the otherPlayer with an x
                    print("hit")
                    otherPlayer.gridShips.changeSingleSpace(shotLocationRow, shotLocationCol, "x")
                    self.gridShots.changeSingleSpace(shotLocationRow, shotLocationCol, "x")
                else : #if the space is water print miss and update both the gridShot of the player and the gridShips of the other player with an o
                    otherPlayer.gridShips.changeSingleSpace(shotLocationRow, shotLocationCol, "o")
                    self.gridShots.changeSingleSpace(shotLocationRow, shotLocationCol, "o")
                    print("miss")
                shotSelection = True
            else : #if the point is not within the grid prompt the user to reenter
                print("input invalid")
                continue

    def stillHasShips(self): #scans each grid and checks if there is a ship value left on the board
        for i in range(10):
            for j in range(10):
                if self.gridShips.returnLocation(i, j) == "S" or "A" or "B" or "C" or "D":
                    return True
        return False
















