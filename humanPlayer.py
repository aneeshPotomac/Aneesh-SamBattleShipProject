from Player import Player

class humanPlayer(Player) :
    def placeShip(self, ship, size):
        while selectionIsValid == False :
            locationRow = input("what row do you want your ship in?")
            locationCol = input("what column do you want your ship in?")
            direction = input("what direction do you want to place the ship")
            selectionIsValid = True
            if direction == "up" and locationRow + size <= 10 :
                for i in range(locationRow + size)  :
                    if not self.gridShips.isSpaceWater(locationRow + i, locationCol) :
                        selectionIsValid = False
            if direction == "down" and locationRow - size >= 0 :
                for i in range(locationRow - size) :
                    if not self.gridShips.isSpaceWater(locationRow - i, locationCol) :
                        selectionIsValid = False
            if direction == "right" and locationCol + size <= 10:
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
            self.gridShips.createShipGrid()
            shotSelection = False
            while shotSelection == False :
                shotLocationRow = input("what row")
                shotLocationCol = input("what column")
                if shotLocationRow <= 10 and shotLocationCol <= 10 :
                    if not self.gridShips.isSpaceWater() :
                        print("hit")
                        self.gridShips.changeSingleSpace(shotLocationRow, shotLocationCol, "x")
                    else :
                        print("miss")

                else :
                    continue













