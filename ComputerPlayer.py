from Player import Player
import random


class ComputerPlayer(Player):
    def __init__(self):
        super().__init__()
    def takeTurn(self, other_player):
        same_num = True
        while same_num:  # making sure we have a different number than previously
            row_col = random.randint(0, 99)
            if row_col <= 9: # if the number is greater than 10 we are in first row
                row = 0
                col = row_col
            else:  # row = first digit column = second digit
                row = row_col // 10
                col = row_col % 10
            if self.gridShots.returnLocation(row, col) == "~":  # check if we haven't shot there before
                same_num = False
        if other_player.gridShips.isSpaceWater(row, col):  # if the spot comp generated is water
            print("you Missed")
            self.gridShots.changeSingleSpace(row, col, "m")
            other_player.gridShips.changeSingleSpace(row, col, "m")
        else: # "otherwise the computer shot"
            print("hit")
            other_player.gridShots.changeSingleSpace(row, col, "h")
            self.gridShips.changeSingleSpace(row, col, "h")
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
    def stillHasShips(self):
        for i in range(10):
            for j in range(10):
                if self.gridShips.returnLocation(i, j) == "S" or "A" or "B" or "C" or "D":
                    return True
        return False

