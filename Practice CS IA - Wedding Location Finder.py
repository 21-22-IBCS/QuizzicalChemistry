from graphics import*
from Button import*

def findvalidwedding(input_loc, input_price, input_pu):
   
    f = open("Wedding Location.txt", "r")

    #string value
    wl = f.read()

    #list value
    wl_list1 = wl.split("\n")


    for i in wl_list1:
        if len(i)==0:
            wl_list1.remove(i)

    del wl_list1[0]
    del wl_list1[len(wl_list1)-1]


    wl_prices = []
   
           
    for i in range(int(len(wl_list1)/3)):
        if "Price: $" in wl_list1[(3*i+2)]:
            prices = wl_list1[(3*i)+2].lstrip("Price: $")
            wl_prices.append(prices)

   

    valid_wedding = []

   
    for i in range(len(wl_list1)):
        if input_loc in wl_list1[i]:
            a = int(((i+2)/3)-1)
            if wl_prices[a] in wl_list1[i+1]:
                valid_wedding.append(wl_list1[i-1])
                valid_wedding.append(wl_list1[i])
                valid_wedding.append(wl_prices[a])
   
   
    valid_wedding2 = []
    for i in range(len(valid_wedding)):
        if i%3==0:
            valid_wedding2.append(valid_wedding[i].strip("<>"))
        else:
            valid_wedding2.append(valid_wedding[i])

    valid_wedding3 = []
    for i in range(int(len(valid_wedding2)/3)):
        a = 2+3*i
        if int(valid_wedding[a]) > int(input_price)-int(input_pu) and int(valid_wedding[a]) < int(input_price)+int(input_pu):
            valid_wedding3.append(valid_wedding2[a-2])
            valid_wedding3.append(valid_wedding2[a-1])
            valid_wedding3.append(valid_wedding2[a])
           

    sorted_wedding = []
    difference1 = 100000
    difference2 = 100000
    difference3 = 100000
    for i in range(int(len(valid_wedding3)/3)):
        a=2+3*i
        abs_uncertainty = abs(int(valid_wedding3[a])-int(input_price))
        if abs_uncertainty < difference1:
            sorted_wedding.insert(0, valid_wedding3[a])
            sorted_wedding.insert(0, valid_wedding3[a-1])
            sorted_wedding.insert(0, valid_wedding3[a-2])
            difference1 = abs_uncertainty
        else:
            if abs_uncertainty < difference2:
                sorted_wedding.insert(3, valid_wedding3[a])
                sorted_wedding.insert(3, valid_wedding3[a-1])
                sorted_wedding.insert(3, valid_wedding3[a-2])
                difference2 = abs_uncertainty
            else:
                if abs_uncertainty < difference3:
                    sorted_wedding.insert(6, valid_wedding3[a])
                    sorted_wedding.insert(6, valid_wedding3[a-1])
                    sorted_wedding.insert(6, valid_wedding3[a-2])
                    difference3 = abs_uncertainty
                else:
                    sorted_wedding.append(valid_wedding3[a-2])
                    sorted_wedding.append(valid_wedding3[a-1])
                    sorted_wedding.append(valid_wedding3[a])
   
           

    return sorted_wedding

def main():

    #Creating user interface
    win = GraphWin("wedding location finder",800,600)
    background = Image(Point(400,300), "wedding_place.gif")
    background.draw(win)
   
    #Text
    title = Text(Point(400,50), "Wedding Where")
    title.setSize(32)
    title.draw(win)
   
    title2 = Text(Point(400,110), "choose the best place for your wedding")
    title2.setSize(18)
    title2.draw(win)
   
    text_loc = Text(Point(400,400), "Location")
    text_loc.setSize(18)
    text_loc.draw(win)
   
    text_price = Text(Point(400,500), "Price")
    text_price.setSize(18)
    text_price.draw(win)
    text_pm = Text(Point(390,550), "+-")
    text_pm.setSize(18)
    text_pm.draw(win)

    #Entry
    loc_en = Entry(Point(390,450), 30)
    loc_en.draw(win)
   
    price_en = Entry(Point(300,550), 15)
    price_en.draw(win)
    pm_en = Entry(Point(480,550), 15)
    pm_en.draw(win)
   
    #Button
    quitB = Button(win, 'red', "QUIT", Point(750,40), 30)
   
    ent_button = Button(win, 'white', "enter", Point(540,500), 30)

    input_loc = ""
    input_price = 0
    input_pu = 0

    while True:
        m = win.getMouse()
       
        if quitB.isClicked(m):
            win.close()
       
        if ent_button.isClicked(m):
            input_loc = loc_en.getText()
            input_price = price_en.getText()
            input_pu = pm_en.getText()
           
            wedding = findvalidwedding(input_loc, input_price, input_pu)
           
               
            if len(wedding) == 0:
                    text_loc.setText("No place found. Enter location again.")
                    text_price.setText("Enter price again.")
       
                   
                   
            else:
       
                text_loc.undraw()
                text_price.undraw()
                text_pm.undraw()
                loc_en.undraw()
                price_en.undraw()
                pm_en.undraw()
                   
                ent_button.undraw()
       
                   
                rec = Rectangle(Point(50,170), Point(750,570))
                rec.draw(win)
       
                hor_line1 = Line(Point(50,230), Point(750,230))
                hor_line1.draw(win)
                hor_line2 = Line(Point(50,315), Point(750,315))
                hor_line2.draw(win)
                hor_line3 = Line(Point(50,400), Point(750,400))
                hor_line3.draw(win)
                hor_line4 = Line(Point(50,485), Point(750,485))
                hor_line4.draw(win)
                   
                ver_line1 = Line(Point(283,170), Point(283,570))
                ver_line1.draw(win)
                ver_line2 = Line(Point(517,170), Point(517,570))
                ver_line2.draw(win)
       
                text_name = Text(Point(167,200), "Name")
                text_name.setSize(18)
                text_name.draw(win)
                text_loc = Text(Point(400,200), "Location")
                text_loc.setSize(18)
                text_loc.draw(win)
                text_price = Text(Point(633,200), "Price")
                text_price.setSize(18)
                text_price.draw(win)
   
                entry1_name = Entry(Point(167,273),17)
                entry1_name.setSize(18)
                entry1_name.draw(win)
                entry1_loc = Entry(Point(401,273),17)
                entry1_loc.setSize(18)
                entry1_loc.draw(win)
                entry1_price = Entry(Point(634,273),17)
                entry1_price.setSize(18)
                entry1_price.draw(win)

                entry2_name = Entry(Point(167,357),17)
                entry2_name.setSize(18)
                entry2_name.draw(win)
                entry2_loc = Entry(Point(401,357),17)
                entry2_loc.setSize(18)
                entry2_loc.draw(win)
                entry2_price = Entry(Point(634,357),17)
                entry2_price.setSize(18)
                entry2_price.draw(win)
       
                entry3_name = Entry(Point(167,441),17)
                entry3_name.setSize(18)
                entry3_name.draw(win)
                entry3_loc = Entry(Point(401,441),17)
                entry3_loc.setSize(18)
                entry3_loc.draw(win)
                entry3_price = Entry(Point(634,441),17)
                entry3_price.setSize(18)
                entry3_price.draw(win)
       
                entry4_name = Entry(Point(167,525),17)
                entry4_name.setSize(18)
                entry4_name.draw(win)
                entry4_loc = Entry(Point(401,525),17)
                entry4_loc.setSize(18)
                entry4_loc.draw(win)
                entry4_price = Entry(Point(634,525),17)
                entry4_price.setSize(18)
                entry4_price.draw(win)

                if 1<=len(wedding):
                    entry1_name.setText(wedding[0])
                    entry1_loc.setText(wedding[1])
                    entry1_price.setText(wedding[2])
                else:
                    entry1_name.setText("No Place Found")
                    entry1_loc.setText("No Place Found")
                    entry1_price.setText("No Place Found")                  
   
                if 4<=len(wedding):
                    entry2_name.setText(wedding[3])
                    entry2_loc.setText(wedding[4])
                    entry2_price.setText(wedding[5])
                else:
                    entry2_name.setText("No Place Found")
                    entry2_loc.setText("No Place Found")
                    entry2_price.setText("No Place Found")
       
                if 7<=len(wedding):
                    entry3_name.setText(wedding[6])
                    entry3_loc.setText(wedding[7])
                    entry3_price.setText(wedding[8])
                else:
                    entry3_name.setText("No Place Found")
                    entry3_loc.setText("No Place Found")
                    entry3_price.setText("No Place Found")
                       
                if 10<=len(wedding):
                    entry4_name.setText(wedding[9])
                    entry4_loc.setText(wedding[10])
                    entry4_price.setText(wedding[11])
                else:
                    entry4_name.setText("No Place Found")
                    entry4_loc.setText("No Place Found")
                    entry4_price.setText("No Place Found")
               
           
       
           
       
       
       
             

if __name__ == "__main__":
    main()
    
