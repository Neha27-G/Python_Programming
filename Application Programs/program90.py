def Display(Arr, iSize):
    iCnt = 0

    print("Elements of array are :")

    for iCnt in range(iSize):
        print(Arr[iCnt])

def main():
    Brr = None
    iLength = int(input("Enter number of Elements :"))

    Brr = [0] * iLength  #memory allocation

    print("Enter the elements :")

    for i in range(iLength):
        Brr[i] = int(input())

    Display(Brr, iLength)

    del Brr

if __name__ == "__main__":
    main()