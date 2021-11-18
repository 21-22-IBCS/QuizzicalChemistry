import time
import random

def mergeSort(li2):
    if len(li2) > 1:
        m = len(li2)//2
        left = li2[:m]
        right = li2[m:]
        mergeSort(left)
        mergeSort(right)
        i, j, k = 0, 0, 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                li2[k] = left[i]
                i += 1
            else:
                li2[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            li2[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            li2[k] = right[j]
            j += 1
            k += 1

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
    #the values(number of random numbers, selection sort time, merge sort time)
    #for the five repeated times are appended each to all_num, all_sel, all_mer
    #so that the total result can be printed at the end of the code
    #which will help the values to be organized
    
    all_num = ["Number: "]
    all_sel = ["Selection Sort: "]
    all_mer = ["Merge Sort: "]
    print("This test will be repeated five times total")
    
    #repeated because the assignment needs to show results at least five times
<<<<<<< HEAD
    for i in range(6):
=======
    for i in range(5):
>>>>>>> 5c3cf4e04c081ed5e67fdc272fefbcc40626a550
        num = int(input("number of random numbers between 1 to 500: "))
        list_diff = []
        list_diff2 = []
        for i in range(10):
            test1=[]
            for i in range(num):
                test1.append(random.randint(1, 500))

            #finding time for selection sort
            start = time.time()
            selectionSort(test1)
            stop = time.time()
            diff1 = stop - start
            list_diff.append(diff1)

            test2=[]
            for i in range(num):
                test2.append(random.randint(1, 500))

            #finding time for merge sort
            start2 = time.time()
            mergeSort(test2)
            stop2 = time.time()
            diff2 = stop2 - start2
            list_diff2.append(diff2)

        all_num.append(num)

        #finding selection sort time for each of the five trials
        total = 0
        for dif in list_diff:
            total = total + dif
        avgTime = total/10
        print("selection sort: " + str(avgTime) + " sec")
        
        all_sel.append(str(avgTime))

        #finding merge sort time for each of the five trials
        total2 = 0
        for dif in list_diff2:
            total2 = total2 + dif
        avgTime2 = total2 / 10

        all_mer.append(str(avgTime2))
        print("merge sort: " + str(avgTime2) + " sec\n")
        
    print(all_num)
    print(all_sel)
    print(all_mer)
    
if __name__ == "__main__":
    main()
