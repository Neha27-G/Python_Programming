def CountFrequency(Arr, iSize):
    iCnt = 0
    iCount = 0

    for iCnt in range(iSize):
        if(Arr[iCnt] == 11):
            iCount += 1

    return iCount

def main():
    Brr = None
    iLength = int(input("Enter number of Elements :"))

    Brr = [0] * iLength  #memory allocation

    print("Enter the elements :")

    for i in range(iLength):
        Brr[i] = int(input())

    iRet = CountFrequency(Brr, iLength)
    print("Frequency : ",iRet)

    del Brr

if __name__ == "__main__":
    main()