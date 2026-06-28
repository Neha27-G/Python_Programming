def CheckEvenOdd(iNo):

    iRemainder = 0
    iRemainder = iNo % 2
    return iRemainder

def main():
    iValue = 0
    iRet = 0
    
    iValue = int(input("Enter the number :"))

    iRet = CheckEvenOdd(iValue)
    
    if(iRet == 0):
        print("Number is Even")

    else:
        print("Number is Odd")

if __name__ == "__main__":
    main()
    
