def CountEvenOddDigits(iNo):
    iCountEven = 0
    iCountOdd = 0

    if(iNo == 0):
        return 1
    
    if(iNo < 0):
        iNo = -iNo

    while(iNo != 0):
        iDigits = iNo % 10

        if((iDigits % 2) == 0):
            iCountEven += 1
        else:
            iCountOdd += 1

        iNo = iNo // 10

    print("Count of Even Numbers :",iCountEven)
    print("Count of Odd Numbers :",iCountOdd)

def main():

    iValue = int(input("Enter the Number :"))

    CountEvenOddDigits(iValue)

if __name__ == "__main__":
    main()