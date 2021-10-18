from Player import Player
import random

class ComputerPlayer(Player):
    arr = []
    for i in range(0, 99):
        arr.append(i)
    def __init__(self):
        self.gridShips = Grid()
        self.gridShots = Grid()
        super().__init__(self)

    def takeTurn(self):
        random.shuffle(arr)
        row_col = arr.pop()
        if row_col < 9:
            row = 1
            col = row_col
        else:
            row = row_col // 10
            col = row_coll % 10
        if otherperson.gridShips.isSpaceWater(row, col):
            print("you Missed")
        else:
            print("hit")
            otherperson.gridShips.changeSingleSpace(row, col, value)


        
        pass

    def placeShip(self, ship, size):
        t = true
        while t:
            a = random.randint(1, 2)  # 1 represents horizontal and 2 is vertical
            b = random.randint(0, 9-size)
            c = random.randint(0, 9-size)
            if a == 1:
                for i in range(size):
                    if isSpaceWater(b, i+c):
                        if i == size:
                            changeRow(b, ship, c, size)
                            t = false
                        continue
                    else:
                        break
            elif a == 2:
                for i in range(size):
                    if isSpaceWater(b+i, c):
                        if i == size:
                            # Col = the col to change
                            # Value = the string to put into the list
                            # rowStart = the start of the row to be changed
                            # size = number of spaces in the row to change
                            changeCol(c, ship, b, size)
                            t = false
                        continue
                    else:
                        break

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

