from Player import Player

class humanPlayer(Player) :
    def placeShip(self, ship, size):
        selectionIsValid = False
        while selectionIsValid == False :
            locationRow = input("what row do you want your ship in?")
            locationCol = input("what column do you want your ship in?")
            direction = input("what direction do you want to place the ship")
            selectionIsValid = True
            if direction == "up" and locationRow + size <= 9 :
                for i in range(locationRow + size)  :
                    if not self.gridShips.isSpaceWater(locationRow + i, locationCol) :
                        selectionIsValid = False
            if direction == "down" and locationRow - size >= 0 :
                for i in range(locationRow - size) :
                    if not self.gridShips.isSpaceWater(locationRow - i, locationCol) :
                        selectionIsValid = False
            if direction == "right" and locationCol + size <= 9:
                for i in range(locationCol + size) :
                    if not self.gridShips.isSpaceWater(locationRow, locationCol + i) :
                        selectionIsValid = False
            if direction == "left" and locationCol - size >= 0 :
                for i in range(locationCol - size) :
                    if not self.gridShips.isSpaceWater(locationRow, locationCol - i):
                        selectionIsValid = False

            if not selectionIsValid :
                continue
            else :
                if direction == "up" or direction == "down" :
                    self.gridShips.changeCol(locationCol , ship , locationRow , size)
                if direction == "right" or direction == "left" :
                    self.gridShips.changeRow(locationRow, ship, locationCol, size)

    def takeTurn(self, otherPlayer):
        shotSelection = False
        while shotSelection == False :
            shotLocationRow = input("what row")
            shotLocationCol = input("what column")
            if shotLocationRow <= 9 and shotLocationCol <= 9 :
                if not otherPlayer.gridShips.isSpaceWater() :
                    print("hit")
                    otherPlayer.gridShips.changeSingleSpace(shotLocationRow, shotLocationCol, "x")
                    self.gridShots.changeSingleSpace(shotLocationRow, shotLocationCol, "x")
                else :
                    otherPlayer.gridShips.changeSingleSpace(shotLocationRow, shotLocationCol, "o")
                    self.gridShots.changeSingleSpace(shotLocationRow, shotLocationCol, "o")
                    print("miss")

            else :
                print("input invalid")
                continue

    def stillHasShips(self):
        for row in range(9) :
            for col in range(9) :
                if self.gridShips.returnLocation(row,col) != "~" or self.gridShips.returnLocation(row,col) != "x" or self.gridShips.returnLocation(row,col) != "o" :
                    return false
                    break
                else :
                    continue
















