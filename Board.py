from graphics import*
from Button import*
from Piece import*
from Nodrawpiece import*

class OthelloBoard():

    def __init__(self, win):
        self.win = win
        
        #matrix of buttons in (column, row) format
        self.cells = []
        for i in range(8):
            rows = []
            for j in range(8):
                rows.append(Button(win, "green", "", Point(i*50 + 100, j*50 + 100), 25))
            self.cells.append(rows)

        #determines black or white
        self.turnCount = 0

        #store all pieces on the board
        self.pieces = []

        #store all piece positions on board
        self.piecePos = []
        
        

    def calculateScore(self):
        blackScore = 0
        whiteScore = 0
        for p in self.pieces:
            if p.getColor() == "black":
                blackScore += 1
            else:
                whiteScore += 1
        print("Black: " + str(blackScore))
        print("White: " + str(whiteScore))
        print(" -------------- ")

    #set up the board to start a game
    def initial(self):
        p0 = Piece(self.win, 3, 3)
        p1 = Piece(self.win, 4, 4)
        p2 = Piece(self.win, 3, 4)
        p3 = Piece(self.win, 4, 3)

        #two of the pieces are black
        p2.change()
        p3.change()
        self.pieces = [p0,p1,p2,p3]
        self.piecePos = [p0.getPos(), p1.getPos(), p2.getPos(), p3.getPos()]

    def capture(self, p):
            #list of directions to start looking for adjacent pieces to change
            directions = []
            #nested loop to add all 8 positions
            for i in range(-1,2):
                for j in range(-1,2):
                    adj = [p.getPos()[0] + i, p.getPos()[1] + j]
                    #don't add [0,0] direction
                    if not (adj == p.getPos()):   
                        directions.append([i,j])

            #initialize list of pieces to change color
            toChange = []
            #loop through all directions
            for d in directions:
                #staged list temporarily adds pieces to be changed
                #may not be changed if there is no "book-end" to the colors
                staged = []
                stop = False
                noPiece = False
                for i in range(1,9):
                    if not (stop or noPiece):
                        noPiece = True
                        nextP = [p.getPos()[0] + i*d[0], p.getPos()[1] + i*d[1]]
                        for piece in self.pieces:
                            if piece.getPos() == nextP:
                                noPiece = False
                                if piece.getColor() == p.getColor():
                                    stop = True
                                    break
                                else:
                                    staged.append(piece)
                    else:
                        break
                
                if not noPiece:
                    for s in staged:
                        toChange.append(s)
                
            for p in toChange:
                p.change()
                
    def checkchange(self, p):
        #list of directions to start looking for adjacent pieces to change
        directions = []
        #nested loop to add all 8 positions
        for i in range(-1,2):
            for j in range(-1,2):
                adj = [p.getPos()[0] + i, p.getPos()[1] + j]
                #don't add [0,0] direction
                if not (adj == p.getPos()):   
                    directions.append([i,j])

        #initialize list of pieces to change color
        toChange = []
        #loop through all directions
        for d in directions:
            #staged list temporarily adds pieces to be changed
            #may not be changed if there is no "book-end" to the colors
            staged = []
            stop = False
            noPiece = False
            for i in range(1,9):
                if not (stop or noPiece):
                    noPiece = True
                    nextP = [p.getPos()[0] + i*d[0], p.getPos()[1] + i*d[1]]
                    for piece in self.pieces:
                        if piece.getPos() == nextP:
                            noPiece = False
                            if piece.getColor() == p.getColor():
                                stop = True
                                break
                            else:
                                staged.append(piece)
                else:
                    break
            
            if not noPiece:
                for s in staged:
                    toChange.append(s)
        
        return toChange
    
    #play a piece on the board given space clicked on board
    #(c, r) = (column, row) of space / "button" clicked
    def play(self, c, r):

        #assume it is a fair place to put a piece
        valid = True
        for piece in self.pieces:
            #if space is already taken by another piece. it is not valid
            if piece.getPos() == [c, r]:
                valid = False
            

        #only create the new piece if it is valid
        if valid:
                p = Piece(self.win, c, r)

                #alternate placing black/white piece based on the turn count
                if self.turnCount%2 == 0:
                        p.change()

                self.pieces.append(p)
                self.piecePos.append(p.getPos())
                self.turnCount += 1
                self.capture(p)

    def minflip(self):
        turn_val = []
        pos = [-1,-1]
        length = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,18,20]
        for i in range(0,8):
            for j in range(0,8):
                p = Nodrawpiece(i,j)
                #print(self.piecePos)
                if p not in self.piecePos:
                    turn_val.append(self.checkchange(p))
                    for k in turn_val:
                        if len(k) != 0:
                            if len(k)<len(length):
                                length = k
                                pos = [i,j]
                                
        return pos

    def maxflip(self):
        turn_val = []
        pos = [-1,-1]
        length = []
        for i in range(0,8):
            for j in range(0,8):
                p = Nodrawpiece(i,j)
                print(self.piecePos)
                if p not in self.piecePos:
                    turn_val.append(self.checkchange(p))
                    for k in turn_val:
                        if len(k) != 0:
                            if len(k)>len(length):
                                length = k
                                pos = [i,j]
        return pos
                    
        
        
        
             

            
