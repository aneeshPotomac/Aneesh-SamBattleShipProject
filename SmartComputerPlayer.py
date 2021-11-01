from Player import Player
import random
class SmartComputerPlayer(Player):
    def __init__(self):
        super().__init__()

    def initialTakeTurn(self,otherPlayer):
        shotLocationRow = random.randint(0, 9)
        shotLocationCol = random.randint(0, 9)
        hit = False
        if not otherPlayer.gridShips.isSpaceWater(shotLocationRow,shotLocationCol):  # if the space is a ship print hit and update both the gridShot of the player and the gidShips of the otherPlayer with an x
            print("hit")
            otherPlayer.gridShips.changeSingleSpace(shotLocationRow, shotLocationCol, "x")
            self.gridShots.changeSingleSpace(shotLocationRow, shotLocationCol, "x")
            global row
            row = shotLocationRow
            global col
            col = shotLocationCol
            return True
        else:  # if the space is water print miss and update both the gridShot of the player and the gridShips of the other player with an o
            otherPlayer.gridShips.changeSingleSpace(shotLocationRow, shotLocationCol, "o")
            self.gridShots.changeSingleSpace(shotLocationRow, shotLocationCol, "o")
            hit = False
            print("miss")
            return False

    def takeTurn(self,otherPlayer):
        # initialTakeTurn()
        up = (row + 1, col)
        down = (row - 1, col)
        right = (row, col + 1)
        left = (row, col - 1)
        multiDirectionalList = [up,down,right,left]
        i = 0
        if initialTakeTurn() == True :
            if not otherPlayer.gridShips.isSpaceWater(multiDirectionalList[i][0], multiDirectionalList[i][1]):  # if the space is a ship print hit and update both the gridShot of the player and the gidShips of the otherPlayer with an x
                print("hit")
                otherPlayer.gridShips.changeSingleSpace(shotLocationRow, shotLocationCol, "x")
                self.gridShots.changeSingleSpace(shotLocationRow, shotLocationCol, "x")
                row = multiDirectionalList[i][0]
                col = multiDirectionalList[i][1]
            else :
                print("miss")
                if i < len(multiDirectionalList) :
                    i = i + 1
                else :
                    initialTakeTurn()

#make a boolean field, if you want to run initial take turn make that boolean true if not make false
#put if statement at bottom to run initialTakeTurn