def SumEven(Arr, iSize):
    iCnt = 0
    iSum = 0

    for iCnt in range(iSize):

        if(Arr[iCnt] % 2 == 0):
            iSum = iSum + Arr[iCnt]

    return iSum

def main():
    Brr = None
    iLength = int(input("Enter number of Elements :\n"))

    Brr = [0] * iLength  #memory allocation

    print("Enter the elements :")

    for i in range(iLength):
        Brr[i] = int(input())

    iRet = SumEven(Brr, iLength)
    print("Summation of Even Elements are : ",iRet)

    del Brr

if __name__ == "__main__":
    main()