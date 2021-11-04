from Player import Player
import random

class SmartComputerPlayer(Player):
    def __init__(self):
        super().__init__()
        self.initialTT = True
        self.hit = False
        self.row = 0
        self.col = 0
        self.i = 0

    def placeShip(self, ship , size ):
        t = True
        while t:
            a = random.randint(1, 2)  # 1 represents horizontal and 2 is vertical
            b = random.randint(0, 10-size)
            c = random.randint(0, 10-size)
            if a == 1:  # if we place horizontally
                for i in range(size):  # when in range size
                    if self.gridShips.isSpaceWater(b, i+c):  # Check the spaces to the right
                        if i == size-1:  # if we are on the last value of i, change the values to ship name
                            self.gridShips.changeRow(b, ship, c, size)
                            t = False
                        continue
                    else:
                        break
            elif a == 2: # If we place vertically
                for i in range(size): # when in range size
                    if self.gridShips.isSpaceWater(b+i, c):  # Check the spaces under
                        if i == size-1:  # if we are on the last value of i, change the values to ship name
                            self.gridShips.changeCol(c, ship, b, size)
                            t = False
                        continue
                    else:
                        break

    def initialTakeTurn(self,otherPlayer):
        same_num = True
        while same_num:  # making sure we have a different number than previously
            row_col = random.randint(0, 99)
            if row_col <= 9:  # if the number is greater than 10 we are in first row
                shotLocationRow = 0
                ShotLocationCol = row_col
            else:  # row = first digit column = second digit
                shotLocationRow = row_col // 10
                shotLocationCol = row_col % 10
            if self.gridShots.returnLocation(shotLocationRow, shotLocationCol) == "~":  # check if we haven't shot there before
                same_num = False
        self.hit = False
        if not otherPlayer.gridShips.isSpaceWater(shotLocationRow,shotLocationCol):  # if the space is a ship print hit and update both the gridShot of the player and the gidShips of the otherPlayer with an x
            print("hit")
            otherPlayer.gridShips.changeSingleSpace(shotLocationRow, shotLocationCol, "x")
            self.gridShots.changeSingleSpace(shotLocationRow, shotLocationCol, "x")
            self.row = shotLocationRow
            self.col = shotLocationCol
            self.hit = True
        else:  # if the space is water print miss and update both the gridShot of the player and the gridShips of the other player with an o
            otherPlayer.gridShips.changeSingleSpace(shotLocationRow, shotLocationCol, "O")
            self.gridShots.changeSingleSpace(shotLocationRow, shotLocationCol, "O")
            self.hit = False
            print("miss")

    def takeTurn(self,otherPlayer):
        # initialTakeTurn()
        up = (self.row - 1, self.col)
        down = (self.row + 1, self.col)
        right = (self.row, self.col + 1)
        left = (self.row, self.col - 1)
        multiDirectionalList = [up,down,right,left]
        #make i a field to reuse it, only set to zero in certain scenarios
        if self.hit == True : # if the random shot was a hit we want to shoot adjacent
            if multiDirectionalList[self.i][0] <= 9 and multiDirectionalList[self.i][0] >= 0 and multiDirectionalList[self.i][1] <= 9 and multiDirectionalList[self.i][1] >= 0 : # check if shot is in range
                if not otherPlayer.gridShips.isSpaceWater(multiDirectionalList[self.i][0], multiDirectionalList[self.i][1]) and otherPlayer.gridShips.returnLocation(multiDirectionalList[self.i][0], multiDirectionalList[self.i][1]) != "O":  # if the space is a ship print hit and update both the gridShot of the player and the gidShips of the otherPlayer with an x
                    print("hit")
                    otherPlayer.gridShips.changeSingleSpace(multiDirectionalList[self.i][0], multiDirectionalList[self.i][1], "x")
                    self.gridShots.changeSingleSpace(multiDirectionalList[self.i][0], multiDirectionalList[self.i][1], "x")
                    self.row = multiDirectionalList[self.i][0]#fix this portion
                    self.col = multiDirectionalList[self.i][1]#fix this portion
                    self.initialTT = False
                else : # if we missed print miss
                    print("miss")
                    otherPlayer.gridShips.changeSingleSpace(multiDirectionalList[self.i][0],multiDirectionalList[self.i][1] , "O")
                    self.gridShots.changeSingleSpace(multiDirectionalList[self.i][0], multiDirectionalList[self.i][1], "O")
                    if self.i < len(multiDirectionalList) :
                        self.i = self.i + 1
                    else :# if we iterate through all the adjacent directins
                        self.i = 0
                        self.hit = False
                        self.initialTT = True
        if self.initialTT == True : #if true run initial take turn
            self.initialTakeTurn(otherPlayer)


    def stillHasShips(self):
        for y in range(10): # we want to check all rows
            for j in range(10):# we want to check all columns to see if they still have ships
                if self.gridShips.returnLocation(y, j) == "S" or "A" or "B" or "C" or "D":
                    return True
        return False

#make a boolean field, if you want to run initial take turn make that boolean true if not make false
#put if statement at bottom to run initialTakeTurn