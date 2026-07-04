def SumFactors(iNo):
    iCnt = 0
    iSum = 0

    for iCnt in range(1,(iNo//2) + 1):   # To reduce time complexity(// means integer division)
        if((iNo % iCnt)== 0):
            iSum = iSum + iCnt
    
    print("Summation of Factors :",iSum)
            

def main():
    iValue = 0

    iValue = int(input("Enter the Number :"))

    SumFactors(iValue)

if __name__ =="__main__":
    main()