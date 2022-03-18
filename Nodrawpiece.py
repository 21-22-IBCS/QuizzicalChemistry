from graphics import *

class Nodrawpiece():
    
     def __init__(self, c, r):
        self.c = c
        self.r = r
        self.pos = [c, r]
        #default to set the piece to white
        self.color = "white"

    #change the color to the other team
    #can be called if capturing pieces or placing a black piece.
     def change(self):
        if self.color == "white":
            self.color = "black"
        else:
            self.color = "white"

    #getPos could be useful for board determing capture or valid play
     def getPos(self):
        return self.pos

    #getColor could be useful for board determing capture or valid play
     def getColor(self):
        return self.color


    
