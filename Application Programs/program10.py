def CheckEvenOdd(iNo):

    if((iNo % 2)== 0):
        return True
    else:
        return False

def main():
    iValue = 0
    bRet = False
    
    iValue = int(input("Enter the number :"))

    bRet = CheckEvenOdd(iValue)
    
    if(bRet == True):
        print(iValue," is Even")

    else:
        print(iValue," is Odd")

if __name__ == "__main__":
    main()
    
