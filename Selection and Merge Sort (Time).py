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
    all_num = ["Number: "]
    all_sel = ["Selective Sort: "]
    for i in range(5):
        num = int(input("number of random numbers between 1 to 500: "))
        list_diff = []
        list_diff2 = []
        for i in range(10):
            test1=[]
            for i in range(num):
                test1.append(random.randint(1, 500))

            start = time.time()
            selectionSort(test1)
            stop = time.time()
            diff1 = stop - start
            list_diff.append(diff1)

            test2=[]
            for i in range(num):
                test2.append(random.randint(1, 500))

            start2 = time.time()
            mergeSort(test2)
            stop2 = time.time()
            diff2 = stop2 - start2
            list_diff2.append(diff2)

        all_num.append(num)

        total = 0
        for dif in list_diff:
            total = total + dif
        avgTime = total/10
        
        all_sel.append(str(avgTime)
        
        total2 = 0
        for dif in list_diff2:
            total2 = total2 + dif
        avgTime2 = total2/10
        print("merge sort: " + str(avgTime2) + " sec\n")

        print(all_num)
        print(all_sel)
if __name__ == "__main__":
    main()
        
