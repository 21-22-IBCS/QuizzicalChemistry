import random
import time

def selectionSort(li):
    sortedList = []
    while len(li) > 0:
        minE = li[0]
        for i in range(len(li)):
            if li[i] < minE:
                minE = li[i]
        li.pop(li.index(minE))
        sortedList.append(minE)

    return sortedList

def main():

    n=100
    differencesSelection = []
    totalTime = 0
    for i in range(10):
        
        test=[]
        for i in range(n):
            test.append(random.randint(1, n))

        start = time.time()
        selectionSort(test)
        end = time.time()
        differencesSelection.append(end-start)

        totalTime = totalTime + float(differencesSelection[i])
        
    average = totalTime/10
    print(average)
    




if __name__ == "__main__":
    main()
