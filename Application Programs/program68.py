def CheckPallindrome(iNo):
    iRev= 0
    temp = 0

    temp = iNo

    while(iNo != 0):
        iDigits = iNo % 10
        iRev = (iRev * 10) + iDigits
        iNo = iNo // 10

    if(temp == iRev):
        return True
    else:
        return False

def main():

    iValue = int(input("Enter the Number :"))

    bRet = CheckPallindrome(iValue)
    
    if(bRet == True):
        print("Number is Pallindrome")
    else:
        print("Number is Not Pallindrome")

if __name__ == "__main__":
    main()