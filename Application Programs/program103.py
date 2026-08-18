def Minimum(Arr, iSize):
    iCnt = 0
    iMin = 0

    iMin = Arr[0]

    for iCnt in range(iSize):

        if(Arr[iCnt] < iMin):
            iMin = Arr[iCnt]

    return iMin

def main():
    Brr = None
    iRet = 0
    iLength = int(input("Enter number of Elements :"))

    Brr = [0] * iLength  #memory allocation

    print("Enter the elements :")

    for i in range(iLength):
        Brr[i] = int(input())

    iRet = Minimum(Brr, iLength)
    print("Minimum elements are :",iRet)

    del Brr

if __name__ == "__main__":
    main()