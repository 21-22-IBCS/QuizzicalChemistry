def gcs(s1, s2):
    subString1 = []
    subString2 = []

    for i in range(len(s1)):
        for k in range(i, len(s1)):
            subString1.append(s1[i:k+1])

    for i in range(len(s2)):
        for k in range(i, len(s2)):
            subString2.append(s2[i:k+1])

    maxS = 0
    result = ""
    for i in range(len(subString1)):
        for k in range(len(subString2)):
            if subString1[i] == subString2[k]:
                if len(subString1[i]) > maxS:
                    maxS = len(subString1[i])
                    result = subString1[i]
    return result

def main():

    s1 = "asdfjkla;sjdf;las"
    s2 = "asjdf;lajsdfl;k"

    gSub = gcs(s1, s2)
    print(gSub)

if __name__ == "__main__":
    main()
