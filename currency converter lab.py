#Exchange Rate Standard: 14:10 02.04.2022 PST


from graphics import*
from Button import*

exchange_rate = {
                "dollars":1.0,
                "won":1198.39,
                "euro":0.87,
                "yuan":6.36,
                "yen":115.2,
                "peso":20.68,
                "rupee":74.64
                }



def ex_dollars(a):
    float_dollars = float(a) * exchange_rate['dollars']
    result = str(float_dollars)
    return result
                
def ex_won(a):
    float_won = float(a) * exchange_rate['won']
    result = str(float_won)
    return result
            
def ex_euro(a):
    float_euro = float(a) * exchange_rate['euro']
    result = str(float_euro)
    return result
def ex_yuan(a):
    float_yuan = float(a) * exchange_rate['yuan']
    result = str(float_yuan)
    return result
    
def ex_yen(a):
    float_yen = float(a) * exchange_rate['yen']
    result = str(float_yen)
    return result

def ex_peso(a):
    float_peso= float(a) * exchange_rate['rupee']
    result = str(float_peso)
    return result


                
def main():
    
    
    win = GraphWin("Currency Converter", 800, 600)



    
    en_button = Button(win, "white", "", Point(150, 40), 45)
    te_button = Button(win, "white", "", Point(300, 40), 45)
    
    close = Button(win, "grey", "Quit", Point(150, 560), 45)
    
    dollar = Button(win, "white", "Dollar", Point(720, 50), 45)
    won = Button(win, "white", "Won", Point(720, 125), 45)
    euro = Button(win, "white", "Euro", Point(720, 200), 45)
    yuan = Button(win, "white", "Yuan", Point(720, 275), 45)
    yen = Button(win, "white", "Yen", Point(720, 350), 45)
    peso = Button(win, "white", "Peso", Point(720, 425), 45)
    rupee = Button(win, "white", "Rupee", Point(720, 500), 45)


    en = Entry(Point(150,40), 10)
    en.draw(win)
    
    win.getMouse()
    str_in = en.getText()
    input_str  = float(str_in)
    

    m = win.getMouse()
    
    while True:
        
        if close.isClicked(m):
            win.close()
            
        if dollar.isClicked(m):
            result = ex_dollars(input_str)
        
        if won.isClicked(m):
            result = ex_won(input_str)
            
        if euro.isClicked(m):
            result = ex_euro(input_str)
            
        if yuan.isClicked(m):
            result = ex_yuan(input_str)
            
        if yen.isClicked(m):
            result = ex_yen(input_str)
            
        if peso.isClicked(m):
            result = ex_peso(input_str)
            
        if rupee.isClicked(m):
            result = ex_rupee(input_str)

        te = Text(Point(300, 40), result)
        te.draw(win)
        
    win.close()
    
if __name__ == "__main__":
    main()
    


