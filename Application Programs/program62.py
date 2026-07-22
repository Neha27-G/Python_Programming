def CountOddDigits(iNo):
    iCount = 0

    if(iNo == 0):
        return 1
    
    if(iNo < 0):
        iNo = -iNo

    while(iNo != 0):
        iDigits = iNo % 10

        if((iDigits % 2) != 0):
            iCount += 1
        iNo = iNo // 10
    return iCount

def main():

    iValue = int(input("Enter the Number :"))

    iRet = CountOddDigits(iValue)
    print("Number of Odd Digits :",iRet)

if __name__ == "__main__":
    main()