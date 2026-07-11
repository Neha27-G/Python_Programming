def CheckPrime(iNo):
    iCnt = 2

    #filter
    if(iNo <= 1):
        return False

    for iCnt in range(2 , (iNo//2) + 1):
        if((iNo % iCnt) == 0):
            break
    
    if iCnt >= ((iNo // 2)):
        return True
    else:
        return False


def main():
    iValue = 0
    bRet = False

    iValue = int(input("Enter the Number :"))

    bRet = CheckPrime(iValue)

    if(bRet == True):
        print("It is a Prime Number")
    else:
        print("It is Not a Prime Number")

if __name__ == "__main__":
    main()