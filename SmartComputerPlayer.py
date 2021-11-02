from Player import Player
import random

class SmartComputerPlayer(Player):
    def __init__(self):
        super().__init__()
        self.initialTT = False
        self.hit = False
        self.row = 0
        self.col = 0

    def initialTakeTurn(self,otherPlayer):
        shotLocationRow = random.randint(0, 9)
        shotLocationCol = random.randint(0, 9)
        self.hit = False
        if not otherPlayer.gridShips.isSpaceWater(shotLocationRow,shotLocationCol):  # if the space is a ship print hit and update both the gridShot of the player and the gidShips of the otherPlayer with an x
            print("hit")
            otherPlayer.gridShips.changeSingleSpace(shotLocationRow, shotLocationCol, "x")
            self.gridShots.changeSingleSpace(shotLocationRow, shotLocationCol, "x")
            self.row = shotLocationRow
            self.col = shotLocationCol
            self.hit = True
        else:  # if the space is water print miss and update both the gridShot of the player and the gridShips of the other player with an o
            otherPlayer.gridShips.changeSingleSpace(shotLocationRow, shotLocationCol, "o")
            self.gridShots.changeSingleSpace(shotLocationRow, shotLocationCol, "o")
            self.hit = False
            print("miss")

    def takeTurn(self,otherPlayer):
        # initialTakeTurn()
        up = (self.row + 1, self.col)
        down = (self.row - 1, self.col)
        right = (self.row, self.col + 1)
        left = (self.row, self.col - 1)
        multiDirectionalList = [up,down,right,left]
        i = 0
        if self.hit == True :
            if multiDirectionalList[i][0] <= 9 and multiDirectionalList[i][1] <= 9:
                if not otherPlayer.gridShips.isSpaceWater(multiDirectionalList[i][0], multiDirectionalList[i][1]):  # if the space is a ship print hit and update both the gridShot of the player and the gidShips of the otherPlayer with an x
                    print("hit")
                    otherPlayer.gridShips.changeSingleSpace(shotLocationRow, shotLocationCol, "x")
                    self.gridShots.changeSingleSpace(shotLocationRow, shotLocationCol, "x")
                    self.row = multiDirectionalList[i][0]
                    self.col = multiDirectionalList[i][1]
                    initialTT = False
                else :
                    print("miss")
                    if i < len(multiDirectionalList) :
                        i = i + 1
                    else :
                        initialTT = True
        if self.initialTT == True :
            initialTakeTurn()


    def stillHasShips(self):
        for i in range(10):
            for j in range(10):
                if self.gridShips.returnLocation(i, j) == "S" or "A" or "B" or "C" or "D":
                    return True
        return False

#make a boolean field, if you want to run initial take turn make that boolean true if not make false
#put if statement at bottom to run initialTakeTurn