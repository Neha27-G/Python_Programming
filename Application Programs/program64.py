def SumDigits(iNo):
    iSum = 0

    if(iNo == 0):
        return 1
    
    if(iNo < 0):
        iNo = -iNo

    while(iNo != 0):
        iDigits = iNo % 10
        iSum = iSum + iDigits
        iNo = iNo // 10
    return iSum

def main():

    iValue = int(input("Enter the Number :"))

    iRet = SumDigits(iValue)
    print("Summation of Digits are :",iRet)

if __name__ == "__main__":
    main()