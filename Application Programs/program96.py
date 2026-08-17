def LinearSearch(Arr, iSize):
    iCnt = 0

    for iCnt in range(iSize):
        if(Arr[iCnt] == 11):
            return True

    return False

def main():
    Brr = None
    bRet = 0
    iLength = int(input("Enter number of Elements :"))

    Brr = [0] * iLength  #memory allocation

    print("Enter the elements :")

    for i in range(iLength):
        Brr[i] = int(input())

    bRet = LinearSearch(Brr, iLength)

    if(bRet == True):
        print("Element is present")
    else:
        print("Element is not present")

    del Brr

if __name__ == "__main__":
    main()