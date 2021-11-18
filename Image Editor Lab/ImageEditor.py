from graphics import*
from Button import*

def brighten(cats):
    for i in range(500):
        for j in range(451):
            rgb = cats.getPixel(i, j)
            if rgb[0]+25<255:
                rgb[0] = rgb[0]+25
            if rgb[1]+25<255:
                rgb[1] = rgb[1]+25
            if rgb[2]+25<255:
                rgb[2] = rgb[2]+25
            cats.setPixel(i, j, color_rgb(rgb[0], rgb[1], rgb[2]))
                
def darken(cats):
     for i in range(500):
        for j in range(451):
            rgb = cats.getPixel(i, j)
            if rgb[0]-25>0:
                rgb[0] = rgb[0]-25
            if rgb[1]-25>0:
                rgb[1] = rgb[1]-25
            if rgb[2]-25>0:
                rgb[2] = rgb[2]-25
            cats.setPixel(i, j, color_rgb(rgb[0], rgb[1], rgb[2]))
            
def blurr(cats):
    for i in range(499):
        for j in range(450):

                
            rgb1 = cats.getPixel(i,j)
            rgb2 = cats.getPixel(i+1, j)
            rgb3 = cats.getPixel(i, j+1)
            if i-1>0:
                rgb4 =cats.getPixel(i-1, j)
            else:
                rgb4 = rgb1
            if j-1>0:
                rgb5 = cats.getPixel(i, j-1)
            else:
                rgb5 = rgb1

            average0 = int((rgb1[0]+rgb2[0]+rgb3[0]+rgb4[0]+rgb5[0])/5)
            average1 = int((rgb1[1]+rgb2[1]+rgb3[1]+rgb4[1]+rgb5[1])/5)
            average2 = int((rgb1[2]+rgb2[2]+rgb3[2]+rgb4[2]+rgb5[2])/5)

            cats.setPixel(i, j, color_rgb(average0, average1, average2))
            
def contrast(cats):
    for i in range(500):
        for j in range(451):
            rgb = cats.getPixel(i, j)

            for k in range(2):
                if rgb[k]<= 127:
                    if rgb[k]-25>0:
                        rgb[k] = rgb[k]-25
                else:
                    if rgb[k]+25<255:
                        rgb[k] = rgb[k]+25
                        
            cats.setPixel(i, j, color_rgb(rgb[0], rgb[1], rgb[2]))    

    
def orange(cats):
    for i in range(500):
        for j in range(451):
            rgb = cats.getPixel(i, j)
            if rgb[0]+50<255:
                rgb[0] = rgb[0]+50
            if rgb[1]+25<255:
                rgb[1] = rgb[1]+25
            cats.setPixel(i, j, color_rgb(rgb[0], rgb[1], rgb[2]))


def inverse(cats):
    for i in range(500):
        for j in range(451):
            rgb = cats.getPixel(i, j)
            for k in range(2):
                rgb[k] = 255-rgb[k]
            cats.setPixel(i, j, color_rgb(rgb[0], rgb[1], rgb[2]))


                
def main():

    win = GraphWin("Image Editor", 800, 600)
    sh = Button(win, "white", "Show", Point(150, 40), 45)
    hi = Button(win, "white", "Hide", Point(300, 40), 45)
    close = Button(win, "grey", "Quit", Point(150, 560), 45)
    bright = Button(win, "white", "Brighten", Point(720, 50), 45)
    dark = Button(win, "white", "Darken", Point(720, 125), 45)
    blur = Button(win, "white", "Blur", Point(720, 200), 45)
    cont = Button(win, "white", "Contrast", Point(720, 275), 45)
    filt = Button(win, "white", "Orange", Point(720, 350), 45)
    filt2 = Button(win, "white", "Inverse", Point(720, 425), 45)
    res = Button(win, "white", "Reset", Point(720, 500), 45)

    cats = Image(Point(400,300), "Cats.png")

    m = win.getMouse()
    while True:
        if close.isClicked(m):
            break
        if sh.isClicked(m):
            cats.undraw()
            cats.draw(win)
        if hi.isClicked(m):
            cats.undraw()
        if dark.isClicked(m):
            darken(cats)
        if bright.isClicked(m):
            brighten(cats)
        if blur.isClicked(m):
            blurr(cats)
        if cont.isClicked(m):
            contrast(cats)
        if filt.isClicked(m):
            orange(cats)
        if filt2.isClicked(m):
            inverse(cats)
        if res.isClicked(m):
            cats = Image(Point(400,300), "Cats.png")
            cats.undraw()
            cats.draw(win)

            
        m = win.getMouse()

    win.close()
    
if __name__ == "__main__":
    main()


