def Summation(Arr, Size):
    i = 0
    iSum = 0

    for i in range(Size):
        iSum = iSum + Arr[i]

    return iSum

def main():
    iLength = 4

    Brr = [0] * iLength

    print("Enter the element :")

    for i in range(iLength):
        Brr[i] = int(input())

    iRet = Summation(Brr, iLength)
    print("Addition of all Elements are : ",iRet)
    
if __name__ == "__main__":
    main()