def ReverseNumber(iNo):
    iRev= 0

    while(iNo != 0):
        iDigits = iNo % 10
        iRev = (iRev * 10) + iDigits
        iNo = iNo // 10

    return iRev

def main():

    iValue = int(input("Enter the Number :"))

    iRet = ReverseNumber(iValue)
    print("Reverse Number is :",iRet)

if __name__ == "__main__":
    main()