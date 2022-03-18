from graphics import*
from Button import*
from Board import*
`
def main():

    win = GraphWin("Othello", 1000, 600)
    #create Board, set as variable "b"
    b = OthelloBoard(win)
    close = Button(win, "red", "EXIT", Point(700,300), 40)
    #initialize board with 4 pieces to start
    b.initial()

    while True:
        
        m = win.getMouse()
        if close.isClicked(m):
            win.close()
            break

        #check all squares on the board to see if they are clicked
        #i = column,  j = row.   range from (0,0) to (7,7)
        for i in range(8):
            for j in range(8):
                if b.cells[i][j].isClicked(m):
                    b.play(i,j)
                    if b.turnCount <= 15:
                        print(b.minflip())
                    if b.turnCount > 15:
                        print(b.maxflip())
                    b.calculateScore()


if __name__ == "__main__":
    main()
