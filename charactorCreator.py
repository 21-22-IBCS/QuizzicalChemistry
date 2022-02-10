from graphics import*
from Button import*

def main():

    win = GraphWin("Charactor Creator", 800, 600)
    

    o = Oval(Point(200,50),Point(600,550))
    o.draw(win)

    big_nose = Button(win, "white", "big nose", Point(50,50), 45)
    nose1 = Polygon(Point(400,200),Point(520,370),Point(280, 370))

    cir_nose = Button(win, "white", "circle nose", Point(145,50), 45)
    nose2 = Circle(Point(400,300),70)

    rec_nose = Button(win, "white", "rec nose", Point(240,50), 45)
    nose3 = Rectangle(Point(350,250),Point(450,350))

    '''noses = ["big nose","circle nose","rec nose"]
    count = 0

    if big_nose.isClicked(m):
        count = count+1
        count = count%3
        sbig_nose.setText(noses[count])'''

    stop = Button(win, "orange", "quit", Point(50, 250), 45)

    oval_mouth = Button(win, "white", "oval mouth", Point(50,100), 45)
    mouth1 = Oval(Point(280,400), Point(520,450))

    line_mouth = Button(win, "white", "line mouth", Point(145,100), 45)
    mouth2 = Line(Point(280,425), Point(520,425))

    oval_eyes = Button(win, "white", "oval eyes", Point(50,150), 45)
    leyes1 = Oval(Point(270,150), Point(370,200))
    reyes1 = Oval(Point(530,150), Point(430,200))

    rec_eyes = Button(win, "white","rec eyes",Point(145,150),45)
    leyes2 = Rectangle(Point(270,150), Point(370,200))
    reyes2 = Rectangle(Point(430,150), Point(530,200))

    glass = Button(win,"cyan","glasses",Point(50,200),45)
    gline1 = Line(Point(370,175),Point(430,175))
    gline2 = Line(Point(270,175),Point(240,150))
    gline3 = Line(Point(530,175),Point(560,150))

    red_eye = Button(win,"red", "red eyes", Point(145,250),45)
    


    noglass = Button(win, "white", "X glasses", Point(145,200),45)    
                  
    while True:
     
        m = win.getMouse()

        if stop.isClicked(m):
            win.close()
            break

        if cir_nose.isClicked(m):
            nose1.undraw()
            nose2.undraw()
            nose3.undraw()
            nose2.draw(win)
        
        if big_nose.isClicked(m):
            nose1.undraw()
            nose2.undraw()
            nose3.undraw()
            nose1.draw(win)

        if rec_nose.isClicked(m):
            nose1.undraw()
            nose2.undraw()
            nose3.undraw()
            nose3.draw(win)

        if oval_mouth.isClicked(m):
            mouth1.undraw()
            mouth2.undraw()
            mouth1.draw(win)

        if line_mouth.isClicked(m):
            mouth1.undraw()
            mouth2.undraw()
            mouth2.draw(win)

        if oval_eyes.isClicked(m):
            leyes1.undraw()
            reyes1.undraw()
            leyes2.undraw()
            reyes2.undraw()
            leyes1.draw(win)
            reyes1.draw(win)

        if rec_eyes.isClicked(m):
            leyes1.undraw()
            reyes1.undraw()
            leyes2.undraw()
            reyes2.undraw()
            leyes2.draw(win)
            reyes2.draw(win)
            
        if glass.isClicked(m):
            gline1.draw(win)
            gline2.draw(win)
            gline3.draw(win)
            

        if noglass.isClicked(m):
            gline1.undraw()
            gline2.undraw()
            gline3.undraw()

        if red_eye.isClicked(m):
            
                  
if __name__ == "__main__":
    main()
