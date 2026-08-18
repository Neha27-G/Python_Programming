def LinearSearch(Arr, iSize , iNo):
    iCnt = 0
    iCount = 0

    for iCnt in range(iSize):

        if(Arr[iCnt] == iNo):
            iCount += 1
            break

    if(iCount == 0):
        return False
    else:
        return True

def main():
    Brr = None
    bRet = 0
    iLength = int(input("Enter number of Elements :"))

    Brr = [0] * iLength  #memory allocation

    print("Enter the elements :")

    for i in range(iLength):
        Brr[i] = int(input())

    iValue = int(input("Enter the Element that you want to search :\n"))
    
    bRet = LinearSearch(Brr, iLength, iValue)

    if(bRet == True):
        print("Element is present")
    else:
        print("Element is not present")

    del Brr

if __name__ == "__main__":
    main()