from Player import Player
import random


class ComputerPlayer(Player):
    arr = []
    for i in range(0, 99):
        arr.append(i)
    def __init__(self):
        super().__init__()

    def takeTurn(self, other_player):
        random.shuffle(arr)
        row_col = arr.pop()
        if row_col < 9:
            row = 1
            col = row_col
        else:
            row = row_col // 10
            col = row_coll % 10
        if other_player.gridShips.isSpaceWater(row, col):
            print("you Missed")
            self.grisShips.changeSingleSpace(row, col, "m")
            other_player.grisShips.changeSingleSpace(row, col, "m")
        else:
            print("hit")
            other_player.gridShips.changeSingleSpace(row, col, "h")
            self.gridShips.changeSingleSpace(row, col, "m")
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
