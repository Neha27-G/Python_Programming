def Summation(Arr, iSize):
    iCnt = 0
    iSum = 0

    for iCnt in range(iSize):
        iSum = iSum + Arr[iCnt]

    return iSum

def main():
    Brr = None
    iLength = int(input("Enter number of Elements :"))

    Brr = [0] * iLength  #memory allocation

    print("Enter the elements :")

    for i in range(iLength):
        Brr[i] = int(input())

    iRet = Summation(Brr, iLength)
    print("Addition of all Elements are : ",iRet)

    del Brr

if __name__ == "__main__":
    main()