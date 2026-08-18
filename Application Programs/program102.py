def Maximum(Arr, iSize):
    iCnt = 0
    iMax = 0

    iMax = Arr[0]

    for iCnt in range(iSize):

        if(Arr[iCnt] > iMax):
            iMax = Arr[iCnt]

    return iMax

def main():
    Brr = None
    iRet = 0
    iLength = int(input("Enter number of Elements :"))

    Brr = [0] * iLength  #memory allocation

    print("Enter the elements :")

    for i in range(iLength):
        Brr[i] = int(input())

    iRet = Maximum(Brr, iLength)
    print("Maximum elements are :",iRet)

    del Brr

if __name__ == "__main__":
    main()