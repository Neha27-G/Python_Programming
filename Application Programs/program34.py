def DisplayFactors(iNo):
    iCnt = 0

    for iCnt in range(1,iNo):
        if((iNo % iCnt)== 0):
            print(iCnt)

def main():
    iValue = 0

    iValue = int(input("Enter the Number :"))

    DisplayFactors(iValue)

if __name__ =="__main__":
    main()