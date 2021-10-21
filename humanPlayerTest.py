from humanPlayer import humanPlayer

class humanPlayerTest() :

    h = humanPlayer()
    h.placeShip("A",5)
    h.printGrids()
    h.placeShip("B",4)
    h.printGrids()
    h.placeShip("C",3)
    h.printGrids()
    h.placeShip("s",3)
    h.printGrids()
    h.placeShip("D",2)
    h.printGrids()


