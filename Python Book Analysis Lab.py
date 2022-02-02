def main():

    
    f = open("sherlock holmes.txt", "r")
    sh = f.read()

    #replacing /n to nothing ("")

    sh_noN = sh.replace("\n", "")

    #lowercase
    sh_low = sh_noN.lower()

    #split in respect to ***, and delete data that is not desired to be analyzed

    sh_list = sh_low.split("***")

    del sh_list[4]
    del sh_list[3]
    del sh_list[1]
    del sh_list[0]

    #Turning list variable to string to use the split function
    sh_str = str(sh_list)

    #Splitting between nothing
    #making it a list variable with no "" values (only words)

    sh_list2 = sh_str.split()


    for i in sh_list2:
        i = i.strip(",!@#$%₩~^&*()/|\'\"")


    # Task 1

    total = 0

    for i in range(len(sh_list2)):
        total = total + len(sh_list2[i])
            
    average = total/len(sh_list2)
    print(average)

    # Task 2

    from collections import Counter
    #using the Counter module to find the most frequent word in the text
    #and how many times that word appears

    a = Counter(sh_list2)
    common = a.most_common(1)

    print(common)

    # Task 3

    num_and = sh_list2.count("and")
    num_but = sh_list2.count("but")
    num_or = sh_list2.count("or")

    per_and = num_and/len(sh_list2) * 100
    per_but = num_but/len(sh_list2) * 100
    per_or = num_or/len(sh_list2) * 100

    print('Percentage of "and" (%): ' + str(per_and))
    print('Percentage of "but" (%): ' + str(per_but))
    print('Percentage of "or" (%): ' + str(per_or))


    # Bonus Task

    for i in range(113, 126):
        print(sh_list2[i], end = " ")









if __name__ == "__main__":
    main()
