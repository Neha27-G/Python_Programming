def SumDigits(iNo):
    iSum = 0

    while(iNo != 0):
        iSum = iSum + iNo % 10
        iNo = iNo // 10
        
    return iSum

def main():

    iValue = int(input("Enter the Number :"))

    iRet = SumDigits(iValue)
    print("Summation of Digits are :",iRet)

if __name__ == "__main__":
    main()