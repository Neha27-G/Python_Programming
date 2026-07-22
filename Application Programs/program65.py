def SumEvenDigits(iNo):
    iSum = 0

    while(iNo != 0):
        iDigits = iNo % 10

        if((iDigits % 2) == 0):
            iSum = iSum + iDigits
        iNo = iNo // 10
    return iSum

def main():

    iValue = int(input("Enter the Number :"))

    iRet = SumEvenDigits(iValue)
    print("Summation of Even Digits are :",iRet)

if __name__ == "__main__":
    main()