from Player import Player
import random


class ComputerPlayer(Player):
    def __init__(self):
        super().__init__()
    def takeTurn(self, other_player):
        same_num = True
        while same_num:
            row_col = random.randint(0, 99)
            if row_col < 9:
                row = 1
                col = row_col
            else:
                row = row_col // 10
                col = row_col % 10
            if self.gridShots.returnLocation(row, col) == "~":
                same_num = False
        if other_player.gridShips.isSpaceWater(row, col):
            print("you Missed")
            self.gridShots.changeSingleSpace(row, col, "m")
            other_player.gridShips.changeSingleSpace(row, col, "m")
        else:
            print("hit")
            other_player.gridShots.changeSingleSpace(row, col, "h")
            self.gridShips.changeSingleSpace(row, col, "h")
    def placeShip(self, ship , size ):
        t = True
        while t:
            a = random.randint(1, 2)  # 1 represents horizontal and 2 is vertical
            b = random.randint(0, 9-size)
            c = random.randint(0, 9-size)
            if a == 1:
                for i in range(size):
                    if self.gridShips.isSpaceWater(b, i+c):
                        if i == size-1:
                            self.gridShips.changeRow(b, ship, c, size)
                            t = False
                        continue
                    else:
                        break
            elif a == 2:
                for i in range(size):
                    if self.gridShips.isSpaceWater(b+i, c):
                        if i == size-1:
                            self.gridShips.changeCol(c, ship, b, size)
                            t = False
                        continue
                    else:
                        break

    def stillHasShips(self):
        pass
        for i in range(10):
            for j in range(10):
          #      if self.gridShips[i, j] != "x" or self.gridShips[i, j] != "~":
                    return true
