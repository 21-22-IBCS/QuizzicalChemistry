from graphics import*

class Piece():

    def __init__(self, win, c, r):
        self.win = win
        self.c = c
        self.r = r
        self.pos = [c, r]
        #the piece graphic is just a circle centered in the space/cell of board
        self.im = Circle(Point(c*50 + 100, r*50 + 100), 23)
        self.im.draw(win)
        #default to set the piece to white
        self.color = "white"
        self.im.setFill("white")

    #change the color to the other team
    #can be called if capturing pieces or placing a black piece.
    def change(self):
        if self.color == "white":
            self.color = "black"
            self.im.setFill("black")
        else:
            self.color = "white"
            self.im.setFill("white")

    #getPos could be useful for board determing capture or valid play
    def getPos(self):
        return self.pos

    #getColor could be useful for board determing capture or valid play
    def getColor(self):
        return self.color


    
