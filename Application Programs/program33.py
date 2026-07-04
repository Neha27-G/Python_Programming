def CheckDivisible(iNo):

    if((iNo % 3 == 0) and (iNo % 5 == 0)):
        return True
    else:
        return False
    
def main():
    iValue = 0
    bRet = False

    iValue= int(input("Enter The Number :"))

    bRet = CheckDivisible(iValue)

    if(bRet == True):
        print("Number is Divisible by 3 and 5")
    else:
        print("Number is Not Divisible by 3 and 5")

if __name__ =="__main__":
    main()