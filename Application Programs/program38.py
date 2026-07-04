def CheckPerfect(iNo):
    iCnt = 0
    iSum = 0

    for iCnt in range(1,(iNo//2) + 1):   # To reduce time complexity(// means integer division)
        if((iNo % iCnt)== 0):
            iSum = iSum + iCnt

    if(iSum == iNo):
        return True
    else:
        return False    
 
def main():
    iValue = 0
    iRet = 0

    iValue = int(input("Enter the Number :"))

    iRet = CheckPerfect(iValue)

    if(iRet == True):
        print("It is Perfect Number")
    else:
        print("It is Not Perfect Number")
        
if __name__ =="__main__":
    main()